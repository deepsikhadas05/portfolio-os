import { BrainCircuit, Music2, TerminalSquare } from "lucide-react";
import { FaGithub } from "react-icons/fa";
import styles from "./Projects.module.css";

const projects = [
  {
    title: "DeepDev",
    status: "In progress",
    description: "An AI-powered portfolio that turns career exploration into a grounded conversation with DeepDev, a RAG-powered digital twin.",
    tags: ["FastAPI", "LangGraph", "RAG", "ChromaDB"],
    icon: TerminalSquare,
    repoUrl: "https://github.com/deepsikhadas05/portfolio-os",
  },
  {
    title: "Brain Tumor Segmentation",
    status: "Deep learning",
    description: "An Attention U-Net workflow for detecting and segmenting brain tumours in MRI scans, from volumetric preprocessing to prediction overlays.",
    tags: ["TensorFlow", "Attention U-Net", "Computer Vision"],
    icon: BrainCircuit,
    repoUrl: "https://github.com/deepsikhadas05/MRI-Brain-Tumor-Detection-Segmentation-using-Attention-U-Net",
  },
  {
    title: "Story Mood Playlist",
    status: "Chrome extension",
    description: "A reading companion that detects a page's emotional tone and recommends matching Spotify playlists through a secure OAuth flow.",
    tags: ["NLP", "Spotify API", "JavaScript"],
    icon: Music2,
    repoUrl: "https://github.com/deepsikhadas05/STORY-MOOD-PLAYLIST",
  },
];

export default function Projects() {
  return (
    <section id="projects" className={styles.projects}>
      <div className={styles.container}>
        <div className={styles.heading}>
          <div>
            <p className={styles.tag}>01 / SELECTED PROJECTS</p>
            <h2>Systems with a little more curiosity built in.</h2>
          </div>
          <p className={styles.intro}>A collection of AI, automation, and human-centred experiments.</p>
        </div>

        <div className={styles.grid}>
          {projects.map(({ title, status, description, tags, icon: Icon, repoUrl }) => (
            <article className={styles.card} key={title}>
              <div className={styles.cardTop}>
                <div className={styles.icon}><Icon size={24} strokeWidth={1.6} /></div>
                <span>{status}</span>
              </div>
              <div>
                <h3>{title}</h3>
                <p>{description}</p>
              </div>
              <div className={styles.cardBottom}>
                <div className={styles.tags}>{tags.map((tag) => <span key={tag}>{tag}</span>)}</div>
                <a
                  className={styles.githubLink}
                  href={repoUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={`Open ${title} repository on GitHub`}
                >
                  <FaGithub size={22} aria-hidden="true" />
                </a>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
