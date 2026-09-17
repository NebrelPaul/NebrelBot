import { FAQ } from "@/components/FAQ";
import { Features } from "@/components/Features";
import { FinalCTA } from "@/components/FinalCTA";
import { Footer } from "@/components/Footer";
import { Hero } from "@/components/Hero";
import { Navbar } from "@/components/Navbar";
import { Showcase } from "@/components/Showcase";
import { SocialProof } from "@/components/SocialProof";
import { Stats } from "@/components/Stats";

export default function Home() {
  return (
    <div id="top" className="relative flex min-h-full flex-col overflow-x-hidden">
      <Navbar />
      <main className="flex-1">
        <Hero />
        <SocialProof />
        <Features />
        <Showcase />
        <Stats />
        <FAQ />
        <FinalCTA />
      </main>
      <Footer />
    </div>
  );
}
