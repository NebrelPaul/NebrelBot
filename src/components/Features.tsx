const features = [
  {
    title: "Ticket System",
    description:
      "Support-Kanäle mit Gründen, Transcripts und Feedback — sauber für Team und Member.",
    icon: (
      <path
        d="M5 7.5A2.5 2.5 0 0 1 7.5 5h9A2.5 2.5 0 0 1 19 7.5v5A2.5 2.5 0 0 1 16.5 15H12l-3.5 3v-3H7.5A2.5 2.5 0 0 1 5 12.5v-5Z"
        stroke="currentColor"
        strokeWidth="1.6"
        fill="none"
      />
    ),
  },
  {
    title: "Moderation",
    description:
      "Warns, Timeouts und Auto-Aktionen mit Logs — ohne Chaos und ohne Command-Spam.",
    icon: (
      <path
        d="M12 3.5 19 7v4.8c0 4.1-2.8 7.8-7 8.7-4.2-.9-7-4.6-7-8.7V7l7-3.5Z"
        stroke="currentColor"
        strokeWidth="1.6"
        fill="none"
      />
    ),
  },
  {
    title: "Willkommen",
    description:
      "Begrüße neue Member mit Embeds, Rollen und Channels — exakt so, wie dein Server tickt.",
    icon: (
      <>
        <circle cx="12" cy="9" r="3.2" stroke="currentColor" strokeWidth="1.6" fill="none" />
        <path
          d="M5.5 18.5c1.6-2.6 3.8-3.9 6.5-3.9s4.9 1.3 6.5 3.9"
          stroke="currentColor"
          strokeWidth="1.6"
          strokeLinecap="round"
          fill="none"
        />
      </>
    ),
  },
  {
    title: "Server Protection",
    description:
      "Raid-Shield, Join-Limits und Captcha-Optionen halten Angriffe draußen.",
    icon: (
      <>
        <rect
          x="7"
          y="10"
          width="10"
          height="9"
          rx="2"
          stroke="currentColor"
          strokeWidth="1.6"
          fill="none"
        />
        <path
          d="M9.5 10V8.2a2.5 2.5 0 0 1 5 0V10"
          stroke="currentColor"
          strokeWidth="1.6"
          fill="none"
        />
      </>
    ),
  },
  {
    title: "Social Alerts",
    description:
      "Twitch, YouTube und mehr — neue Streams und Uploads landen direkt im Channel.",
    icon: (
      <path
        d="M4.5 8.5h15M6 8.5v8.2A1.8 1.8 0 0 0 7.8 18.5h8.4a1.8 1.8 0 0 0 1.8-1.8V8.5M9.5 5.5h5"
        stroke="currentColor"
        strokeWidth="1.6"
        strokeLinecap="round"
        fill="none"
      />
    ),
  },
  {
    title: "Team Tools",
    description:
      "Rechte, Stats und Workflows für Mods — damit Support und Moderation skalieren.",
    icon: (
      <>
        <circle cx="9" cy="9" r="2.4" stroke="currentColor" strokeWidth="1.6" fill="none" />
        <circle cx="16" cy="10" r="2" stroke="currentColor" strokeWidth="1.6" fill="none" />
        <path
          d="M4.8 17.5c1.1-1.9 2.7-2.9 4.5-2.9 1.1 0 2.1.3 2.9.9M12.8 17.5c.7-1.2 1.8-1.9 3.2-1.9 1.1 0 2 .4 2.7 1.1"
          stroke="currentColor"
          strokeWidth="1.6"
          strokeLinecap="round"
          fill="none"
        />
      </>
    ),
  },
];

export function Features() {
  return (
    <section id="features" className="relative scroll-mt-24 py-24 sm:py-28">
      <div className="mx-auto w-full max-w-6xl px-5 sm:px-8">
        <div className="max-w-2xl">
          <p className="section-label">
            <span className="h-1.5 w-1.5 rounded-full bg-accent" />
            Features
          </p>
          <h2 className="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">
            Alles, was starke Server brauchen
          </h2>
          <p className="mt-3 text-base leading-relaxed text-fg-muted sm:text-lg">
            Module, die du aktivierst — und im Dashboard in Minuten fertig
            konfigurierst.
          </p>
        </div>

        <div className="mt-12 grid gap-x-8 gap-y-10 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((feature) => (
            <article key={feature.title} className="group">
              <div className="mb-4 inline-flex h-11 w-11 items-center justify-center rounded-2xl border border-line bg-accent-soft text-accent transition group-hover:border-accent/40 group-hover:bg-[rgba(47,230,192,0.2)]">
                <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden>
                  {feature.icon}
                </svg>
              </div>
              <h3 className="font-display text-xl font-bold tracking-tight">
                {feature.title}
              </h3>
              <p className="mt-2 text-sm leading-relaxed text-fg-muted sm:text-[0.95rem]">
                {feature.description}
              </p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
