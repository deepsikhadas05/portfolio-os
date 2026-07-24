"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import KineticGrid from "@/components/KineticGrid";
import Typewriter from "@/components/Typewriter";
import StaggeredMenu from "@/components/StaggeredMenu";
import BookDemoButton from "@/components/book-demo-button"; 
import DeepDev from "@/components/DeepDev/DeepDev";


const menuItems = [
  {
    label: "About",
    ariaLabel: "About Me",
    link: "#about",
  },
  {
    label: "Projects",
    ariaLabel: "Projects",
    link: "#projects",
  },
  {
    label: "Experience",
    ariaLabel: "Experience",
    link: "#experience",
  },
  {
    label: "Research",
    ariaLabel: "Research",
    link: "#research",
  },
];

const socialItems = [
  {
    label: "GitHub",
    link: "https://github.com/deepsikhadas05",
  },
  {
    label: "LinkedIn",
    link: "https://www.linkedin.com/in/deepsikha-das-347976253/",
  },
  {
    label: "Email",
    link: "deepsikha1104@gmail.com",
  },
];


export default function Home() {
  const [openDeepDev, setOpenDeepDev] = useState(false);
  
  return (
    <main className="relative h-screen w-screen overflow-hidden bg-black">

      {/* Background */}
      <KineticGrid
        background="#000000"
        dotColor="#ffffff"
        lineColor="#8b5cf6"
        trailColor="#a855f7"
        spacing={22}
        radius={350}
        strength={5}
        trail
      />
      <div
        className={`transition-opacity duration-300 ${
          openDeepDev ? "opacity-0 pointer-events-none" : "opacity-100"
        }`}
      >
      

      {/* Menu */}
      <StaggeredMenu
        isFixed
        position="right"
        items={menuItems}
        socialItems={socialItems}
        displaySocials
        displayItemNumbering={false}
        menuButtonColor="#ffffff"
        openMenuButtonColor="#760FFF"
        changeMenuColorOnOpen
        colors={["#760FFF", "#A855F7"]}
        accentColor="#760FFF"
      />
      </div>
      {/* Top Left Text */}
      <div className="absolute top-0 left-0 z-8">
        <Typewriter
          texts={[
            "Deepsikha",
            "Developer",
            "Builder",
            "Learner",
            "Explorer",
            "Creator",
          ]}
          style={{
            position: "absolute",
            top: "200px",
            left: "100px",
          }}
          prefix=">"
          color="#760FFF"
          typedColor="#ffffff"
          cursorColor="#ffffff"
        />
        <div
        style={{
          position: "absolute",   // Change to "relative" if needed
          top: "280px",           // Vertical position
          left: "90px",          // Horizontal position
          width: "600px",         // Box width
          padding: "24px",        // Inner spacing
          borderRadius: "16px",   // Rounded corners
          background: "transparent"
        }}
      >
        <p
          style={{
            fontFamily: "Prompt",      // Font
            fontSize: "16px",         // Font size
            fontWeight: 350,          // 300-700
            lineHeight: "1.6",
            color: "#d1d5db",
            textAlign: "left",        // left | center | right
            letterSpacing: "0.5px",
          }}
        >
          Hi, I'm <span className="text-white font-semibold">Deepsikha Das</span>,
          <br />
          CSE undergrad with a deep interest in AI/ML and automation. I like to sprinkle 
          a pinch of creativity in my projects and love to go down the rabbit-hole of various 
          topics. There's a lot more to know about me, but I'll leave that upto your curiosity 
          (I promise I'm fun) 
          <br />
          <span className="text-white font-semibold">Talk to my AI-twin to learn more about me ↴</span>
          
        </p>
        <div className="mt-6 ml-78">
          <BookDemoButton
              variant = "violet"
              onClick={() => setOpenDeepDev(true)}
          >
              Meet My AI Twin
          </BookDemoButton>
        </div>
        </div>
        
      </div>  
      {openDeepDev && (
      <DeepDev
        onClose={() => setOpenDeepDev(false)}
      />
      )}
    </main>
    
    
  );
  
}