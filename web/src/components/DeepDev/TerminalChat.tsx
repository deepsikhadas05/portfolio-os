"use client";
import { askAI } from "@/lib/chat";
import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";

type Message = {
  role: "user" | "assistant";
  content: string;
};

const INTRO_MESSAGE: Message = {
  role: "assistant",
  content:
    "Hey! I'm **DeepDev**, Deepsikha's AI twin. Ask me about her projects, internship experience, AI work, certifications, or technical skills.",
};

export default function TerminalChat() {
  const [messages, setMessages] = useState<Message[]>([INTRO_MESSAGE]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [threadId] = useState(() =>
    crypto.randomUUID()
  );

  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  async function sendMessage() {
    if (!input.trim() || loading) return;

    const question = input.trim();

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: question,
      },
    ]);

    setInput("");
    setLoading(true);

    
    // Replaced with FastAPI 
    // -------------------------

    try {
        const result = await askAI(
            threadId,
            question
        );

        setMessages((prev) => [
            ...prev,
            {
            role: "assistant",
            content: result.answer,
            },
        ]);
        } catch (err) {
        console.error(err);

        setMessages((prev) => [
            ...prev,
            {
            role: "assistant",
            content:
                "Sorry, I'm unable to reach DeepDev right now.",
            },
        ]);
        } finally {
        setLoading(false);
        }
  }

  return (
    <div className="flex h-full flex-col">

      {/* Terminal Output */}

      <div className="flex-1 overflow-y-auto px-8 py-8 font-mono">

        <div className="space-y-8">

          {messages.map((message, index) => (
            <div key={index}>

              <div
                className={`mb-2 font-semibold ${
                  message.role === "user"
                    ? "text-white"
                    : "text-[#760FFF]"
                }`}
              >
                {message.role === "user"
                  ? "> you"
                  : "> deepdev"}
              </div>

              <div className="max-w-none font-mono text-[15px] leading-7 text-white/80">
                <ReactMarkdown
                    components={{
                    h1: ({ children }) => (
                        <h1 className="mb-3 text-2xl font-bold text-[#760FFF]">
                        {children}
                        </h1>
                    ),

                    h2: ({ children }) => (
                        <h2 className="mb-2 mt-5 text-xl font-semibold text-[#a855f7]">
                        {children}
                        </h2>
                    ),

                    h3: ({ children }) => (
                        <h3 className="mb-2 mt-4 text-lg font-semibold text-white">
                        {children}
                        </h3>
                    ),

                    p: ({ children }) => (
                        <p className="mb-3 leading-7">
                        {children}
                        </p>
                    ),

                    ul: ({ children }) => (
                        <ul className="mb-3 ml-5 list-disc space-y-1">
                        {children}
                        </ul>
                    ),

                    ol: ({ children }) => (
                        <ol className="mb-3 ml-5 list-decimal space-y-1">
                        {children}
                        </ol>
                    ),

                    li: ({ children }) => (
                        <li>{children}</li>
                    ),

                    strong: ({ children }) => (
                        <strong className="font-semibold text-white">
                        {children}
                        </strong>
                    ),

                    code: ({ children }) => (
                        <code className="rounded bg-[#1a1a1a] px-1.5 py-0.5 text-[#c084fc]">
                        {children}
                        </code>
                    ),
                    }}
                >
                    {message.content}
                </ReactMarkdown>
                </div>

            </div>
          ))}

          {loading && (
            <div>

              <div className="mb-2 font-semibold text-[#760FFF]">
                &gt; deepdev
              </div>

              <div className="flex items-center gap-2">

                <span>Thinking</span>

                <span className="animate-pulse text-[#760FFF]">
                  ▋
                </span>

              </div>

            </div>
          )}

          <div ref={bottomRef} />

        </div>

      </div>

      {/* Terminal Input */}

      <form
        className="border-t border-white/10 bg-[#0d0d0d] p-6"
        onSubmit={(event) => {
          event.preventDefault();
          sendMessage();
        }}
      >

        <div className="flex items-center gap-4 font-mono">

          <span className="text-xl font-bold text-[#760FFF]" aria-hidden="true">
            &gt;
          </span>

          <span className="-ml-3 animate-pulse text-xl text-[#a855f7]" aria-hidden="true">
            ▍
          </span>

          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask DeepDev anything..."
            autoFocus
            disabled={loading}
            className="flex-1 bg-transparent text-white outline-none placeholder:text-white/30 disabled:cursor-not-allowed"
          />

          <button
            type="submit"
            disabled={!input.trim() || loading}
            className="rounded-lg border border-[#760FFF]/70 px-4 py-2 text-sm font-semibold text-[#d8b4fe] transition hover:bg-[#760FFF] hover:text-white disabled:cursor-not-allowed disabled:opacity-40"
          >
            {loading ? "Sending..." : "Send"}
          </button>

        </div>

      </form>

    </div>
  );
}
