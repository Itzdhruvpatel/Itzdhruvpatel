<p align="center">
  <img src="assets/hero.webp" width="100%" alt="A black Lamborghini Aventador on a wet garage floor under a red neon sign reading Dhruv's Garage. Dhruv Patel, IT at DJSCE, Mumbai."/>
</p>

<p align="center">
  <a href="https://atlas-psi-neon-19.vercel.app"><b>Try to beat ATLAS</b></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/dhruv-patel-077765292/"><b>LinkedIn</b></a>
</p>

Most of what I build answers one question: can you trust what the machine just told you? ATLAS asks it of an AI agent reading a poisoned document. TrustCheck asks it of a message that sounds like your boss. AgriX asks it of a crop diagnosis a farmer has to act on. DJS NSS is where I learned to ship for real people on a real deadline.

Every project in this garage gets its own car, because I like cars nearly as much as I like shipping.

**01** [ATLAS](#atlas), AI agent firewall &nbsp;&nbsp;|&nbsp;&nbsp; **02** [TrustCheck](#trustcheck), deepfake defence &nbsp;&nbsp;|&nbsp;&nbsp; **03** [AgriX](#agrix), smart farming &nbsp;&nbsp;|&nbsp;&nbsp; **04** [DJS NSS](#djs-nss), community platforms

**Also in the garage:** [tool wall](#tool-wall) &nbsp;&nbsp;|&nbsp;&nbsp; [hard parts](#hard-parts) &nbsp;&nbsp;|&nbsp;&nbsp; [the numbers](#numbers) &nbsp;&nbsp;|&nbsp;&nbsp; [logbook](#logbook) &nbsp;&nbsp;|&nbsp;&nbsp; [on the lift](#on-the-lift) &nbsp;&nbsp;|&nbsp;&nbsp; [telemetry](#telemetry)

<img src="assets/workshop.webp" width="100%" alt="Spec sheet over a close-up of an orange Lamborghini. AI security: built and tested a prompt injection firewall on a real LLM. Machine learning: compared four CNNs on accuracy against size. Full stack: React, FastAPI and Docker, deployed live with CI. Shipping: live demos, automated tests, honest limits."/>

---

<a id="atlas"></a>

## 01 · ATLAS

*A firewall that stops hidden instructions in documents from hijacking an AI agent.*

<a href="https://atlas-psi-neon-19.vercel.app"><img src="assets/bay-atlas.webp" width="100%" alt="Orange Lamborghini Aventador SVJ under an ATLAS neon sign. In a small test on one real model, 3 of 12 attacks leaked a fake secret with no firewall and 0 of 12 with it on, and 18 of 20 normal tasks still passed."/></a>

Ask an agent to summarize a PDF, and a line hidden in that PDF can tell it to email your data to someone else. ATLAS sits between the agent and its tools: it cleans what comes in, checks where every address came from, plants a canary secret, and replays risky calls without the document to see who really caused them. The numbers come from a small test on one model, and the repo says exactly what they don't prove.

`Python` `FastAPI` `React` `Three.js` `Docker`

[Live arena](https://atlas-psi-neon-19.vercel.app) &nbsp;|&nbsp; [Repo](https://github.com/Itzdhruvpatel/Atlas)

---

<a id="trustcheck"></a>

## 02 · TrustCheck

*Most deepfake tools ask "is this fake?" TrustCheck asks "should you act on this?"*

<img src="assets/bay-trustcheck.webp" width="100%" alt="Blue BMW M4 under a TrustCheck neon sign. It scores four signals per message and has a live Chrome call guard."/>

It scores the media, the wording, who the message claims to come from and what it asks you to do, then makes you verify before any money or data moves. A Chrome extension listens in during live Meet, Zoom and Teams calls. Built with my team for D3COY.

`FastAPI` `Three.js` `Chrome extension` `Python`

[Repo](https://github.com/D3C0Y-1-0/Semicolons_D3C0Y_DhruvPatel)

---

<a id="agrix"></a>

## 03 · AgriX

*Crop recommendations and plant disease detection for farmers.*

<img src="assets/bay-agrix.webp" width="100%" alt="Lamborghini R6 tractor under green light. Crop recommendation accuracy 98.7 percent, disease detection accuracy 90.22 percent, across more than 90,000 images."/>

A Random Forest picks the crop. Four deep learning models competed on disease detection: EfficientNetB0 won on accuracy at 90.22%, while MobileNetV2 reached 89.23% with just 3.4M parameters, small enough for a phone. And yes, that's a Lamborghini. They made tractors before they made supercars.

`Python` `TensorFlow` `Scikit-Learn`

---

<a id="djs-nss"></a>

## 04 · DJS NSS

*The official National Service Scheme site at DJSCE, plus its event sign-up portals.*

<img src="assets/bay-nss.webp" width="100%" alt="BMW M5 CS under a DJS NSS neon sign. Hundreds of student registrations across two event portals."/>

Redesigned the official site with the team and built the Grainathon and Blood Donation Drive registration portals, which handled hundreds of student sign-ups.

`React` `Tailwind CSS`

---

<a id="tool-wall"></a>

## The tool wall

*Every drawer is a skill group.*

<img src="assets/tools.webp" width="100%" alt="Red roller tool cabinet under a neon sign reading The Tool Wall. Languages and web: Python, C++, Java, C, JavaScript, HTML, CSS, Node.js. Data and ML: TensorFlow, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn. Frameworks and tools: React, Tailwind, FastAPI, Three.js, SQL, Docker, Git, Vercel. Foundations: DSA, DAA, DBMS, OS, MIS, Corporate Finance."/>

<details>
<summary><b>Parts list as text</b></summary>
<br>

**Languages and web:** `Python` `C++` `Java` `C` `JavaScript` `HTML` `CSS` `Node.js`

**Data and ML:** `TensorFlow` `Scikit-Learn` `Pandas` `NumPy` `Matplotlib` `Seaborn`

**Frameworks and tools:** `React` `Tailwind CSS` `FastAPI` `Three.js` `SQL` `Docker` `Git` `Vercel`

**Foundations:** `DSA` `DAA` `DBMS` `OS` `MIS` `Corporate Finance`

</details>

---

<a id="hard-parts"></a>

## Hard parts

*Not everything I build runs on a server.*

<img src="assets/hardware.webp" width="100%" alt="Close-up of a tractor's rear tyre in a dark garage. Drip irrigation that optimizes water distribution, and a multi-stage water purifier that removes physical and chemical impurities."/>

---

<a id="numbers"></a>

## The numbers

<img src="assets/glovebox.webp" width="100%" alt="Close-up of a blue BMW M4. B.Tech in IT at DJSCE, 2024 to 2028. CGPA 9.49. Oracle Certified Foundations Associate, 95 percent. 90 plus LeetCode problems solved. AWS Cloud Practitioner Essentials. Deloitte Technology Job Simulation."/>

---

<a id="logbook"></a>

## Logbook

*Technical Co-Committee Member, DJS NSS, since July 2025.*

<img src="assets/service.webp" width="100%" alt="Rear view of a BMW M5 in a dark garage. Service record: 35 kg contributed at Grainathon 3.0, 5 NSS drives and programmes, 2 registration workflows built."/>

- **Data accountability:** built real-time registration workflows for Grainathon and the Blood Donation Drive.
- **Operations:** managed team operations during the NSS Rural Camp and awareness rallies.
- **Fund It Up:** built business models and data-backed financial forecasts in the campus entrepreneurship competition.
- **Service recognition:** Grainathon 3.0, NSS Rural Camp, Andheri Blood Donation Drive, Juhu Beach Cleanup and Vegan Outreach.

---

<a id="on-the-lift"></a>

## On the lift

**Can repeating an attack fool a defence that checks what caused an action?** ATLAS replays risky calls without the suspicious document. In an early test on one model, an attack repeated three times got past the defences I tried, 10 out of 10. That may partly come from how replay keeps history, so I'm testing it properly before writing it up as a paper.

---

<a id="telemetry"></a>

## Telemetry

<img src="assets/telemetry.svg" width="100%" alt="Timing screen showing my weekly GitHub contributions over the last 12 months, refreshed daily."/>

---

<a href="https://atlas-psi-neon-19.vercel.app"><img src="assets/finish.webp" width="100%" alt="Rear of a black Lamborghini with its tail lights glowing in the dark. End of the lap. Thanks for stopping by the garage."/></a>

<p align="center">
  <a href="https://atlas-psi-neon-19.vercel.app"><b>Try to beat ATLAS</b></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/dhruv-patel-077765292/"><b>Talk to me on LinkedIn</b></a>
</p>

<sub>3D cars, rendered by me in Three.js with my own lighting and some repainting, all <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>: <a href="https://sketchfab.com/3d-models/lamborghini-aventador-svj-sdc-free-784e4656aca649cca55d6b18740a19b2">Lamborghini Aventador SVJ</a> by SDC PERFORMANCE, <a href="https://sketchfab.com/3d-models/bmw-m4-f82-8e87379f40fd40dcac0a751e22c1a188">BMW M4 F82</a> by Black Snow, <a href="https://sketchfab.com/3d-models/lamborghini-tractor-r6-125-dcr-wwwvecarzcom-56d7c8e7e2cb4d15a3d80cc42c697c53">Lamborghini Tractor R6</a> by vecarz, <a href="https://sketchfab.com/3d-models/bmw-m5-cs-f90-8f74fb3420e24213aaeea33dc99450a3">BMW M5 CS</a> by fvrenbld. BMW and Lamborghini are trademarks of their owners. This is a fan profile with no affiliation.</sub>
