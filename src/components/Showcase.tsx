import { DashboardMock } from "./DashboardMock";

export function Showcase() {
  return (
    <section
      id="dashboard"
      className="relative scroll-mt-24 overflow-hidden border-y border-line bg-[linear-gradient(180deg,rgba(16,24,41,0.55),rgba(6,9,18,0))] py-24 sm:py-28"
    >
      <div
        className="pointer-events-none absolute -left-24 top-10 h-72 w-72 rounded-full bg-signal/20 blur-3xl"
        aria-hidden
      />
      <div
        className="pointer-events-none absolute -right-16 bottom-0 h-80 w-80 rounded-full bg-accent/15 blur-3xl"
        aria-hidden
      />

      <div className="relative mx-auto grid w-full max-w-6xl items-center gap-12 px-5 lg:grid-cols-[0.95fr_1.05fr] sm:px-8">
        <div>
          <p className="section-label">
            <span className="h-1.5 w-1.5 rounded-full bg-accent" />
            Dashboard
          </p>
          <h2 className="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">
            Steuere alles im Browser — nicht über Commands
          </h2>
          <p className="mt-4 max-w-lg text-base leading-relaxed text-fg-muted sm:text-lg">
            Module an/aus, Rechte, Channels und Automationen. NebrelBot gibt dir
            die Kontrolle, die wachsende Communities erwarten.
          </p>

          <ul className="mt-8 space-y-4">
            {[
              "Live-Übersicht für Tickets, Joins und Auto-Mods",
              "Module mit einem Klick aktivieren",
              "Einstellungen, die dein ganzes Team versteht",
            ].map((item) => (
              <li key={item} className="flex items-start gap-3 text-sm text-fg sm:text-base">
                <span className="mt-1 inline-flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-accent-soft text-accent">
                  <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden>
                    <path
                      d="M2.5 6.2 4.8 8.5 9.5 3.5"
                      stroke="currentColor"
                      strokeWidth="1.7"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                </span>
                {item}
              </li>
            ))}
          </ul>

          <a href="#cta" className="btn-primary mt-9 inline-flex">
            Zum Dashboard
          </a>
        </div>

        <div className="relative">
          <div className="absolute -inset-3 rounded-[1.6rem] bg-[linear-gradient(135deg,rgba(47,230,192,0.2),rgba(91,140,255,0.12),transparent)] blur-xl" />
          <div className="relative scale-[0.98] sm:scale-100">
            <DashboardMock />
          </div>
        </div>
      </div>
    </section>
  );
}
