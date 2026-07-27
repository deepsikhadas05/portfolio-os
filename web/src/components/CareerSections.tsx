"use client";

import { ArrowUpRight, Boxes, FlaskConical, ServerCog, Sparkles } from "lucide-react";
import { useEffect, useRef, useState } from "react";

const focus = [
  ["AI systems", "Retrieval-augmented experiences that make complex knowledge useful and conversational."],
  ["Applied ML", "Computer vision and deep-learning pipelines that move from messy data to interpretable outcomes."],
  ["Automation", "Reliable developer and infrastructure workflows designed to remove repetitive work."],
];

export default function CareerSections() {
  const experienceRef = useRef<HTMLElement>(null);
  const [timelineVisible, setTimelineVisible] = useState(false);

  useEffect(() => {
    const section = experienceRef.current;
    if (!section) return;
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        setTimelineVisible(true);
        observer.disconnect();
      }
    }, { threshold: 0.3 });
    observer.observe(section);
    return () => observer.disconnect();
  }, []);

  return <>
    <section id="experience" ref={experienceRef} className={`portfolio-section experience-section ${timelineVisible ? "timeline-visible" : ""}`}>
      <div className="section-kicker">02 / EXPERIENCE</div>
      <div className="experience-layout">
        <div><h2 className="section-title">Building dependable systems at scale.</h2><p className="timeline-note">A small chapter with a very large operational footprint.</p></div>
        <div className="timeline-wrap">
          <div className="timeline-line" aria-hidden="true"><span /></div>
          <p className="timeline-date timeline-date-end">Jul 2026</p>
          <p className="timeline-date timeline-date-start">Jul 2025</p>
          <article className="timeline-card timeline-main">
            <div className="timeline-node"><span /><Sparkles size={15} /></div>
            <div className="timeline-top"><div><p className="role">Infrastructure Engineer Intern</p><h3>A.P. Moller — Maersk</h3></div><span>12 months · Pune, India</span></div>
            <p>Worked with Fleet IT Infrastructure on automation, offline patching, virtual-machine provisioning, and enterprise support for maritime environments.</p>
            <div className="timeline-points"><span><ServerCog size={17} /> Automation-first operations</span><span><Boxes size={17} /> Enterprise deployment workflows</span></div>
          </article>
          <div className="timeline-coda"><span className="coda-dot" /><p>From keeping systems steady<br />to building the next thing.</p></div>
        </div>
      </div>
    </section>

    <section id="research" className="portfolio-section research-section">
      <div className="section-kicker">03 / RESEARCH & EXPLORATION</div>
      <div className="research-heading"><h2 className="section-title">Learning in public, building with intent.</h2><p>My current exploration lives at the intersection of intelligent systems, practical machine learning, and thoughtful automation.</p></div>
      <div className="focus-grid">{focus.map(([title, text], index) => <article className="focus-card" key={title}><div><FlaskConical size={21}/><span>0{index + 1}</span></div><h3>{title}</h3><p>{text}</p><ArrowUpRight size={20} /></article>)}</div>
    </section>
  </>;
}
