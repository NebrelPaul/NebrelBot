const communities = [
  "Aurora Hub",
  "Night Shift",
  "Pixel Forge",
  "Echo Lounge",
  "Nova Guild",
  "Orbit Labs",
  "Signal Room",
  "Drift Collective",
];

export function SocialProof() {
  const track = [...communities, ...communities];

  return (
    <section className="py-16 sm:py-20">
      <div className="mx-auto w-full max-w-6xl px-5 sm:px-8">
        <p className="text-center text-sm font-semibold uppercase tracking-[0.16em] text-fg-dim">
          Gebaut für Communities, die wachsen
        </p>
        <div className="marquee mt-8">
          <div className="marquee-track">
            {track.map((name, i) => (
              <span
                key={`${name}-${i}`}
                className="font-display text-2xl font-bold tracking-tight text-fg/35 sm:text-3xl"
              >
                {name}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
