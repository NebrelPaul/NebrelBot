"use client";

import { useEffect, useRef, useState } from "react";

const stats = [
  { label: "Server bereit", value: 1200, suffix: "+", decimals: 0 },
  { label: "Commands / Tag", value: 2.4, suffix: "M", decimals: 1 },
  { label: "Uptime", value: 99.9, suffix: "%", decimals: 1 },
];

export function Stats() {
  const ref = useRef<HTMLElement>(null);
  const [active, setActive] = useState(false);

  useEffect(() => {
    const node = ref.current;
    if (!node) return;
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setActive(true);
          observer.disconnect();
        }
      },
      { threshold: 0.35 },
    );
    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  return (
    <section ref={ref} className="py-10 sm:py-14">
      <div className="mx-auto grid w-full max-w-6xl gap-8 px-5 sm:grid-cols-3 sm:px-8">
        {stats.map((stat) => (
          <div key={stat.label} className="text-center sm:text-left">
            <p className="font-display text-4xl font-extrabold tracking-tight text-fg sm:text-5xl">
              <CountUp
                active={active}
                value={stat.value}
                decimals={stat.decimals}
              />
              <span className="text-accent">{stat.suffix}</span>
            </p>
            <p className="mt-2 text-sm font-semibold text-fg-muted">{stat.label}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

function CountUp({
  active,
  value,
  decimals,
}: {
  active: boolean;
  value: number;
  decimals: number;
}) {
  const [n, setN] = useState(0);

  useEffect(() => {
    if (!active) return;
    const start = performance.now();
    const duration = 1200;
    let frame = 0;

    const tick = (now: number) => {
      const t = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - t, 3);
      setN(value * eased);
      if (t < 1) frame = requestAnimationFrame(tick);
    };

    frame = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(frame);
  }, [active, value]);

  return <>{n.toFixed(decimals)}</>;
}
