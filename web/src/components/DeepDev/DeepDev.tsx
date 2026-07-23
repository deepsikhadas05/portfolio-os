"use client";

import { useState } from "react";
import TerminalChat from "./TerminalChat";

interface DeepDevProps {
  onClose: () => void;
}

export default function DeepDev({ onClose }: DeepDevProps) {
  const [started, setStarted] = useState(false);

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

          <div className="flex-1 overflow-hidden">

            {!started ? (
              <div className="flex h-full flex-col">

                {/* Welcome */}

                <main className="flex-1 overflow-y-auto">

                  <div className="mx-auto flex h-full max-w-5xl flex-col px-10 py-14">

                    <div className="animate-in fade-in duration-500">

                      <h2 className="text-5xl font-bold text-white">
                        Heyy !
                      </h2>

                      <p className="mt-6 text-xl leading-9 text-white/70">
                        I'm{" "}
                        <span className="font-semibold text-[#760FFF]">
                          DeepDev
                        </span>
                        , Deepsikha's AI Twin.
                      </p>

                      <p className="mt-4 max-w-3xl text-lg leading-8 text-white/50">
                        I can answer questions about her projects,
                        internship, infrastructure engineering
                        experience, AI work, certifications and
                        technical skills.
                      </p>

                      <p className="mt-4 max-w-3xl text-lg leading-8 text-white/50">
                        Type CHAT to talk to DeepDev ~
                      </p>

                    </div>

                  </div>

                </main>

                {/* Terminal Input */}

                <footer className="shrink-0 border-t border-white/10 bg-[#0D0D0D]">

                  <TerminalChat
                    onFirstMessage={() => setStarted(true)}
                  />

                </footer>

              </div>
            ) : (
              <div className="h-full animate-in fade-in duration-500">
                <TerminalChat />
              </div>
            )}

          </div>

        </div>
      </div>
    </div>
  );
}