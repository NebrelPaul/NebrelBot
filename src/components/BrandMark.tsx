export function BrandMark({ className = "" }: { className?: string }) {
  return (
    <span className={`inline-flex items-center gap-2.5 ${className}`}>
      <span
        aria-hidden
        className="relative grid h-9 w-9 place-items-center overflow-hidden rounded-xl"
        style={{
          background:
            "linear-gradient(145deg, rgba(47,230,192,0.95), rgba(91,140,255,0.85))",
          boxShadow: "0 0 0 1px rgba(255,255,255,0.12), 0 10px 30px rgba(47,230,192,0.25)",
        }}
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
          <path
            d="M12 3.5 19 7.2v9.6L12 20.5 5 16.8V7.2L12 3.5Z"
            stroke="#041018"
            strokeWidth="1.6"
          />
          <path
            d="M8.2 12.1c1.1 1.7 2.3 2.6 3.8 2.6s2.7-.9 3.8-2.6"
            stroke="#041018"
            strokeWidth="1.6"
            strokeLinecap="round"
          />
          <circle cx="9.2" cy="10.2" r="1" fill="#041018" />
          <circle cx="14.8" cy="10.2" r="1" fill="#041018" />
        </svg>
      </span>
      <span className="font-display text-[1.15rem] font-extrabold tracking-tight">
        Nebrel<span className="text-accent">Bot</span>
      </span>
    </span>
  );
}
