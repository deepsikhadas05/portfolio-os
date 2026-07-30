import TerminalChat from "./TerminalChat";

interface DeepDevProps {
  onClose: () => void;
}

export default function DeepDev({ onClose }: DeepDevProps) {
  return (
    <div className="fixed inset-0 z-[999999] bg-black/80 backdrop-blur-md animate-in fade-in duration-300">
      <div className="mx-auto flex h-screen max-w-[1800px] flex-col p-6">
        <div className="flex h-full flex-col overflow-hidden rounded-3xl border border-[#760FFF]/30 bg-[#090909] shadow-[0_0_50px_rgba(118,15,255,0.15)]">

          {/* ================= HEADER ================= */}

          <header className="flex h-20 shrink-0 items-center justify-between border-b border-white/10 px-8">

            <button
              onClick={onClose}
              className="text-sm font-medium text-white/60 transition hover:text-white"
            >
              ← Back
            </button>

            <div className="flex items-center gap-3">
              <span className="h-3 w-3 rounded-full bg-green-500 animate-pulse" />

              <h1 className="text-3xl font-bold tracking-wide text-white">
                DeepDev
              </h1>
            </div>

            <button
              onClick={onClose}
              className="text-2xl text-white/50 transition hover:text-red-400"
            >
              ×
            </button>

          </header>

          {/* ================= BODY ================= */}

          <div className="flex-1 overflow-hidden animate-in fade-in duration-500">
            <TerminalChat />
          </div>

        </div>
      </div>
    </div>
  );
}
