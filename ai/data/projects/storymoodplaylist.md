---
id: project_story_mood_playlist

title: Story Mood Playlist

type: project

status: Completed

priority: 80

visibility: public

category: AI Application

repository: story-mood-playlist

skills:
  - JavaScript
  - Python
  - NLP
  - Chrome Extension API
  - Spotify Web API
  - OAuth 2.0
  - PKCE
  - REST API
  - HTML
  - CSS

last_updated: 2024-09-01
---

# Overview

Story Mood Playlist is an AI-powered Chrome extension that analyzes the emotional tone of the webpage a user is reading and recommends Spotify playlists that match the detected mood.

The extension combines Natural Language Processing (NLP), Chrome Extension APIs, and Spotify's Web API to create an interactive reading experience where music dynamically complements the content being consumed.

---

# Motivation

People often listen to music while reading articles, blogs, or stories, but manually searching for playlists that match the mood interrupts the experience.

The goal of this project was to automate this process by using AI to understand the emotional context of the content and instantly recommend playlists that enhance the reading experience.

---

# Objectives

The primary objectives of this project were:

- Detect the emotional tone of webpage content using NLP.
- Recommend Spotify playlists that match the detected mood.
- Implement secure Spotify authentication using OAuth 2.0 with PKCE.
- Allow users to refine recommendations using genre and language filters.
- Build a polished and responsive Chrome extension.

---

# Architecture

The project is composed of several independent components.

## Chrome Extension

Built using JavaScript and Chrome Extension APIs.

Responsibilities:

- Capture webpage content
- Trigger mood analysis
- Display detected mood
- Present playlist recommendations
- Manage user interactions

---

## Mood Analysis Engine

Built using Python.

Responsibilities:

- Process extracted webpage text
- Perform NLP-based sentiment analysis
- Classify emotional tone
- Return the detected mood to the extension

Supported moods include:

- Happy
- Sad
- Romantic
- Calm
- Inspirational
- Exciting
- Emotional

---

## Spotify Integration

Built using Spotify's Web API.

Responsibilities:

- Authenticate users
- Search mood-specific playlists
- Retrieve playlist metadata
- Apply user-selected filters
- Return curated playlist recommendations

Authentication uses OAuth 2.0 Authorization Code Flow with PKCE for enhanced security.

---

# Workflow

The recommendation pipeline follows this sequence:

User Opens Webpage

↓

Extension Extracts Text

↓

NLP Mood Analysis

↓

Mood Classification

↓

Spotify Playlist Search

↓

Genre & Language Filtering

↓

Recommended Playlist Display

---

# Features

Key features include:

- NLP-based mood detection from webpage content
- Spotify playlist recommendations
- Genre-based filtering
- Language-based filtering
- Secure OAuth 2.0 (PKCE) authentication
- Interactive Chrome extension interface
- Smooth animated UI with a custom purple theme

---

# Technologies

Programming

- JavaScript
- Python

Frontend

- HTML
- CSS
- Chrome Extension APIs

AI / NLP

- Natural Language Processing
- Sentiment Analysis

APIs

- Spotify Web API
- REST APIs

Authentication

- OAuth 2.0
- PKCE

---

# My Contributions

I independently developed the complete extension, including:

- Chrome extension architecture
- Webpage text extraction
- NLP-based mood detection pipeline
- Spotify API integration
- OAuth 2.0 PKCE authentication
- Playlist recommendation logic
- Genre and language filtering
- User interface design and implementation

---

# Challenges

Major technical challenges included:

- Extracting meaningful text from diverse webpage structures
- Accurately mapping sentiment analysis results to music moods
- Implementing Spotify OAuth 2.0 with PKCE
- Managing secure access tokens
- Integrating REST APIs within Chrome extension constraints
- Designing a responsive extension popup UI

---

# Key Learnings

This project strengthened my understanding of:

- Chrome Extension development
- Natural Language Processing
- Sentiment analysis
- Spotify Web API integration
- OAuth 2.0 Authorization Flow
- PKCE authentication
- REST API integration
- Frontend UI development
- Browser extension architecture

---

# Resume Summary

Developed an AI-powered Chrome extension that performs NLP-based sentiment analysis on webpage content and recommends Spotify playlists through REST API integration. Implemented secure Spotify authentication using OAuth 2.0 with PKCE and built customizable playlist filtering based on genre and language.

---

# Interview Talking Points

## What problem does this solve?

The extension enhances the reading experience by automatically recommending music that matches the emotional tone of the content, eliminating the need for users to manually search for suitable playlists.

## Why use OAuth 2.0 with PKCE?

PKCE provides a secure authentication mechanism for public clients such as Chrome extensions by preventing authorization code interception and eliminating the need to expose client secrets.

## How does mood detection work?

The extension extracts textual content from the active webpage, processes it using an NLP-based sentiment analysis pipeline, classifies the dominant emotional tone, and uses that classification to query Spotify for relevant playlists.

## Biggest Technical Challenge

The most challenging aspect was securely integrating Spotify authentication using OAuth 2.0 with PKCE while coordinating communication between the browser extension, backend services, and Spotify APIs.

---

# Future Improvements

Potential future enhancements include:

- Emotion intensity scoring
- Personalized recommendations based on listening history
- Support for additional music platforms
- Multilingual sentiment analysis
- LLM-powered contextual mood understanding
- Playlist generation instead of playlist search
- User preference learning

---

# Keywords

Chrome Extension, NLP, Sentiment Analysis, Spotify Web API, OAuth 2.0, PKCE, JavaScript, Python, REST API, Browser Extension, Music Recommendation System, AI Application, Natural Language Processing