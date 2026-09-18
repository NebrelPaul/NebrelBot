"use client";

import { useState } from "react";

const faqs = [
  {
    q: "Was ist NebrelBot?",
    a: "NebrelBot ist ein Discord Bot mit Web-Dashboard. Du steuerst Moderation, Tickets, Willkommen und Automationen zentral im Browser — statt alles über Slash-Commands zu verdrahten.",
  },
  {
    q: "Ist NebrelBot kostenlos?",
    a: "Die Kernfunktionen sind kostenlos nutzbar. Premium-Module und White-Label folgen später — für den Start reicht der Free-Tier völlig aus.",
  },
  {
    q: "Wie richte ich den Bot ein?",
    a: "Bot einladen, Server auswählen, Dashboard öffnen und Module aktivieren. Die wichtigsten Permissions setzt Discord beim Invite automatisch.",
  },
  {
    q: "Brauche ich Coding-Kenntnisse?",
    a: "Nein. Alles läuft über das Dashboard. Für Power-User kommen später Webhooks und eine API dazu.",
  },
];

export function FAQ() {
  const [open, setOpen] = useState<number | null>(0);

  return (
    <section id="faq" className="scroll-mt-24 py-24 sm:py-28">
      <div className="mx-auto grid w-full max-w-6xl gap-10 px-5 lg:grid-cols-[0.85fr_1.15fr] sm:px-8">
        <div>
          <p className="section-label">
            <span className="h-1.5 w-1.5 rounded-full bg-accent" />
            FAQ
          </p>
          <h2 className="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">
            Klar, bevor du startest
          </h2>
          <p className="mt-3 max-w-md text-base text-fg-muted">
            Kurze Antworten. Wenn etwas fehlt — schreib uns im Support.
          </p>
        </div>

        <div className="divide-y divide-line border-y border-line">
          {faqs.map((item, index) => {
            const isOpen = open === index;
            return (
              <div key={item.q}>
                <button
                  type="button"
                  className="flex w-full items-center justify-between gap-4 py-5 text-left"
                  aria-expanded={isOpen}
                  onClick={() => setOpen(isOpen ? null : index)}
                >
                  <span className="font-display text-lg font-bold tracking-tight">
                    {item.q}
                  </span>
                  <span
                    className={`grid h-8 w-8 shrink-0 place-items-center rounded-full border border-line text-accent transition ${
                      isOpen ? "rotate-45 bg-accent-soft" : ""
                    }`}
                  >
                    +
                  </span>
                </button>
                <div
                  className={`grid transition-[grid-template-rows] duration-300 ${
                    isOpen ? "grid-rows-[1fr]" : "grid-rows-[0fr]"
                  }`}
                >
                  <div className="overflow-hidden">
                    <p className="pb-5 text-sm leading-relaxed text-fg-muted sm:text-base">
                      {item.a}
                    </p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
