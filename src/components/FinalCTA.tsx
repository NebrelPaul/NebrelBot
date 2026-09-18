export function FinalCTA() {
  return (
    <section id="cta" className="scroll-mt-24 px-5 pb-24 sm:px-8 sm:pb-28">
      <div className="relative mx-auto max-w-6xl overflow-hidden rounded-[2rem] border border-line-strong px-6 py-14 sm:px-12 sm:py-16">
        <div
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              "radial-gradient(ellipse 70% 80% at 15% 20%, rgba(47,230,192,0.22), transparent 55%), radial-gradient(ellipse 60% 70% at 85% 80%, rgba(91,140,255,0.22), transparent 55%), linear-gradient(180deg, #0e1628, #090e1a)",
          }}
          aria-hidden
        />
        <div className="relative mx-auto max-w-2xl text-center">
          <p className="font-display text-4xl font-extrabold tracking-tight sm:text-5xl">
            Nebrel<span className="text-accent">Bot</span>
          </p>
          <h2 className="mt-3 font-display text-2xl font-bold tracking-tight sm:text-3xl">
            Dein Server. Deine Regeln. Ein Dashboard.
          </h2>
          <p className="mx-auto mt-4 max-w-lg text-base text-fg-muted">
            Lade den Bot ein und richte dein erstes Modul in unter fünf Minuten
            ein.
          </p>
          <div className="mt-8 flex flex-col items-center justify-center gap-3 sm:flex-row">
            <a href="#" className="btn-primary min-w-[190px]">
              Bot jetzt einladen
            </a>
            <a href="#features" className="btn-ghost min-w-[190px]">
              Features ansehen
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}
