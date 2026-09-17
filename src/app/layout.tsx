import type { Metadata } from "next";
import { Manrope, Syne } from "next/font/google";
import "./globals.css";

const syne = Syne({
  variable: "--font-syne",
  subsets: ["latin"],
  weight: ["500", "600", "700", "800"],
});

const manrope = Manrope({
  variable: "--font-manrope",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800"],
});

export const metadata: Metadata = {
  title: "NebrelBot — Discord Bot für moderne Communities",
  description:
    "Moderation, Tickets, Willkommen und Automationen — alles in einem Dashboard. NebrelBot macht deinen Discord-Server smarter.",
  openGraph: {
    title: "NebrelBot",
    description:
      "Der Discord Bot mit Dashboard, der deine Community professionell managt.",
    type: "website",
  },
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="de"
      className={`${syne.variable} ${manrope.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-bg text-fg">{children}</body>
    </html>
  );
}
