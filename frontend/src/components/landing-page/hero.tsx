import { ArrowRight } from "lucide-react";
import { Button } from "../ui/button";

const BG_IMAGE =
  "https://images.unsplash.com/photo-1745509267699-1b1db256601e?auto=format&fit=crop&w=1920&q=80";

export default function Hero() {
  return (
    <section
      className="relative w-full h-screen flex items-center justify-center bg-cover bg-center bg-fixed"
      style={{ backgroundImage: `url('${BG_IMAGE}')` }}
    >
      <div className="absolute inset-0 bg-[#000000eb]" />

      <div className="relative z-10 text-center text-white mx-auto w-full max-w-2xl">
        <h1 className="font-serif font-bold text-3xl sm:text-4xl md:text-5xl lg:text-6xl">
          Smart stock analysis,<br></br> made{" "}
          <i className="text-(--green-hero)">simple.</i>
        </h1>
        <p className="text-[#d8d8d8f7] mt-6">
          Enter any ticker. Get a clear, AI-generated analysis with <br></br>{" "}
          actionable insights — without the financial jargon.
        </p>
        <div className="mt-7 mb-7">
          <Button
            variant="signup"
            className="text-sm bg-transparent border border-white/40 hover:bg-white/10 text-white px-4 py-2.5"
          >
            Sign in
          </Button>
          <Button variant="signup" className="text-sm px-4 py-2.5 ml-3">
            Start for free <ArrowRight />
          </Button>
        </div>
        <div>
          <p className="text-xs text-[#717070f7]">No credit card required</p>
        </div>
      </div>
    </section>
  );
}
