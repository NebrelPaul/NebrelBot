import { BrandMark } from "./BrandMark";

export function Footer() {
  return (
    <footer className="border-t border-line py-10">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-8 px-5 sm:flex-row sm:items-center sm:justify-between sm:px-8">
        <div>
          <BrandMark />
          <p className="mt-3 max-w-sm text-sm text-fg-dim">
            Discord Bot & Dashboard für Communities, die professionell wirken
            wollen — ohne Setup-Chaos.
          </p>
        </div>
        <div className="flex flex-wrap gap-x-6 gap-y-2 text-sm font-semibold text-fg-muted">
          <a href="#features" className="hover:text-fg">
            Features
          </a>
          <a href="#dashboard" className="hover:text-fg">
            Dashboard
          </a>
          <a href="#faq" className="hover:text-fg">
            FAQ
          </a>
          <a href="#" className="hover:text-fg">
            Discord
          </a>
        </div>
      </div>
      <div className="mx-auto mt-8 w-full max-w-6xl px-5 text-xs text-fg-dim sm:px-8">
        © {new Date().getFullYear()} NebrelBot. Alle Rechte vorbehalten.
      </div>
    </footer>
  );
}
