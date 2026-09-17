export function DashboardMock() {
  return (
    <div className="relative overflow-hidden rounded-[1.35rem] border border-line-strong bg-[linear-gradient(180deg,#121b2e_0%,#0b1220_100%)] shadow-[0_40px_120px_rgba(0,0,0,0.45),0_0_0_1px_rgba(255,255,255,0.03)]">
      <div className="flex items-center gap-2 border-b border-line px-4 py-3">
        <span className="h-2.5 w-2.5 rounded-full bg-[#ff6b8a]" />
        <span className="h-2.5 w-2.5 rounded-full bg-[#ffc857]" />
        <span className="h-2.5 w-2.5 rounded-full bg-[#2fe6c0]" />
        <span className="ml-3 text-xs font-semibold tracking-wide text-fg-dim">
          dash.nebrelbot.app
        </span>
      </div>

      <div className="grid min-h-[340px] grid-cols-[72px_1fr] sm:grid-cols-[180px_1fr]">
        <aside className="border-r border-line bg-[rgba(8,12,22,0.7)] p-3 sm:p-4">
          <div className="mb-5 hidden items-center gap-2 sm:flex">
            <div className="h-8 w-8 rounded-lg bg-[linear-gradient(135deg,#2fe6c0,#5b8cff)]" />
            <div>
              <p className="text-xs font-bold">NebrelBot</p>
              <p className="text-[10px] text-fg-dim">Server Dashboard</p>
            </div>
          </div>
          <div className="space-y-1.5">
            {["Übersicht", "Moderation", "Tickets", "Willkommen", "Automationen"].map(
              (item, i) => (
                <div
                  key={item}
                  className={`rounded-lg px-2.5 py-2 text-[11px] font-semibold sm:text-xs ${
                    i === 0
                      ? "bg-accent-soft text-accent"
                      : "text-fg-dim hover:bg-white/5"
                  }`}
                >
                  <span className="sm:inline">{item}</span>
                </div>
              ),
            )}
          </div>
        </aside>

        <div className="space-y-4 p-4 sm:p-5">
          <div className="flex flex-wrap items-end justify-between gap-3">
            <div>
              <p className="text-[11px] font-semibold uppercase tracking-[0.14em] text-accent">
                Live Overview
              </p>
              <h3 className="font-display text-lg font-bold sm:text-xl">
                Nebula Community
              </h3>
            </div>
            <div className="rounded-full border border-line bg-white/5 px-3 py-1 text-[11px] font-semibold text-fg-muted">
              <span className="mr-1.5 inline-block h-1.5 w-1.5 rounded-full bg-accent" />
              Online · 1.284 Members
            </div>
          </div>

          <div className="grid gap-3 sm:grid-cols-3">
            {[
              { label: "Offene Tickets", value: "12", tone: "text-warning" },
              { label: "Auto-Mods heute", value: "47", tone: "text-accent" },
              { label: "Neue Joins", value: "89", tone: "text-signal" },
            ].map((stat) => (
              <div
                key={stat.label}
                className="rounded-xl border border-line bg-white/[0.03] px-3 py-3"
              >
                <p className="text-[10px] font-semibold uppercase tracking-wide text-fg-dim">
                  {stat.label}
                </p>
                <p className={`mt-1 font-display text-2xl font-bold ${stat.tone}`}>
                  {stat.value}
                </p>
              </div>
            ))}
          </div>

          <div className="grid gap-3 lg:grid-cols-[1.2fr_0.8fr]">
            <div className="rounded-xl border border-line bg-white/[0.03] p-3">
              <div className="mb-3 flex items-center justify-between">
                <p className="text-xs font-bold">Aktivität (7 Tage)</p>
                <p className="text-[10px] text-fg-dim">+18%</p>
              </div>
              <div className="flex h-24 items-end gap-1.5">
                {[40, 55, 48, 70, 62, 84, 78].map((h, i) => (
                  <div
                    key={i}
                    className="flex-1 rounded-t-md bg-[linear-gradient(180deg,rgba(47,230,192,0.9),rgba(91,140,255,0.35))]"
                    style={{ height: `${h}%` }}
                  />
                ))}
              </div>
            </div>

            <div className="rounded-xl border border-line bg-white/[0.03] p-3">
              <p className="mb-3 text-xs font-bold">Module</p>
              <div className="space-y-2.5">
                {[
                  { name: "Ticket System", on: true },
                  { name: "Raid Shield", on: true },
                  { name: "Level Rewards", on: false },
                ].map((mod) => (
                  <div
                    key={mod.name}
                    className="flex items-center justify-between text-xs"
                  >
                    <span className="text-fg-muted">{mod.name}</span>
                    <span
                      className={`relative h-5 w-9 rounded-full ${
                        mod.on ? "bg-accent/30" : "bg-white/10"
                      }`}
                    >
                      <span
                        className={`absolute top-0.5 h-4 w-4 rounded-full transition ${
                          mod.on
                            ? "right-0.5 bg-accent"
                            : "left-0.5 bg-fg-dim"
                        }`}
                      />
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
