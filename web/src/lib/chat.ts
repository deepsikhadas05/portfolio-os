const API_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function askAI(
  threadId: string,
  question: string
) {
  const response = await fetch(`${API_URL}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      thread_id: threadId,
      question,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to contact DeepDev");
  }

  return response.json();
}