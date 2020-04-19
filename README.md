<h1 align="center">⛩  🏗 Smart Classroom ⌨ 🔥 </h1>

<h4 align="center"> An Embedded Systems and IoT 2nd Semester Project | Ease your class workflow by automating classroom access without the need of staff to open them for you. (Unless, you want to open parts of the room that is not designed to be accessed to you...)
</h4>
<div align="center">

![Code Formatter](https://img.shields.io/badge/Code%20Formatter-YAPF-important)
![GitHub License](https://img.shields.io/github/license/CodexLink/SmartClassroomSystem?color=purple&label=Repo%20License)
</div>

<div align="center">

![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/codexlink/SmartClassroomSystem/master?label=CodeFactor%20Code%20Quality&logo=codefactor&logoColor=white)
![Codacy Branch Grade](https://img.shields.io/codacy/grade/f649c48ccc3a431a84cad2f7e7ac65ca/master?label=Codacy%20Code%20Quality&logo=codacy&logoColor=White)
![Dependabot Dependency Status](https://badgen.net/dependabot/CodexLink/SmartClassroomSystem/?icon=dependabot)

</div>

# Welcome

## Table of Contents

## "How it really works?"

## 🔥 📁 File Structure Deconstruction
This repository contains a lot of varieties. Meaning you really have to know the path you're going before navigating any further without realizing where the heck are you even going... Just read it in a bare-minimum way and you will be fine 💯

```text
. <Repo Root Folder>/
├── .dependabot/ # Contains Dependabot Dependency Configuration...
│   └── config.yml
│
├── .github/ # Contains Workflow File...
│   └── workflow/
│       └── SketchWorker.yml # It is a sketch validator and worker. It outputs whether those sketches inside of the folder `NodeSketch_SC` will work or uploadable in MCU's memory.
│
├── .vscode/ # VSCode configuration.
│   └── *.json
│
├── Externals/
│   ├── AdLibs/ # Contains acknowledgement by talking to self on how to do it | Specifically made for CodexLink
│   │   └── *.md
│   │
│   ├── Commands/ # Contains only few preset commands that can be used to certain extreme conditions.
│   │   └── *.txt
│   │
│   ├── Project Plan/ # It consists of important notes to look up from what should be context of the project.
│   │   └── * .md
│   │
│   └── Sketch/
│       └── NodeSketch_SC/ # Specifically for NodeMCU Sketches.
│           ├── *.cpp
│           ├── *.h
│           └── *.ino
│
├── SmartClassroom/ # Django Project Folder
│   ├── DataSetBackups/
│   │   └── *.json
│   │
│   ├── NodeHandler/ # Django Micro App. This acknowledges any IoT MCUs by their own POST requests. This app could make changes to the databases.
│   │   ├── migrations/
│   │   │   ├── __pycache__/
│   │   │   │   └── *.pyc
│   │   │   │
│   │   │   └── __init__.py
│   │   │
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── SCControlSystem/ # Django Main Web App. This renders EVERYTHING that any user could access to...
│   │   ├── externs/
│   │   │   ├── __pycache__/
│   │   │   │   └── *.pyc
│   │   │   │
│   │   │   └── __init__.py
│   │   │
│   │   ├── management/
│   │   │   ├── __pycache__/
│   │   │   │   └── *.pyc
│   │   │   │
│   │   │   └── commands/
│   │   │       ├── backup_datasets.py
│   │   │       ├── create_definitive_groups.py
│   │   │       └── get_all_permissions.py
│   │   │
│   │   ├── migrations/ # Literally migrations...
│   │   │   ├── __pycache__/
│   │   │   │   └── *.pyc
│   │   │   │
│   │   │   └── __init__.py
│   │   │   └── ***(migrations_auto_...).py
│   │   │
│   │   ├── scripts/
│   │   │   ├── __pycache__/
│   │   │   │   └── *.pyc
│   │   │   │
│   │   │   └── SC_DSH.py # A script used by SC_ScriptInst.py. It was instantiated (spawns another window) to acknowledge IoT device communicating with the server. Requires Django-Extension to use this script.
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── SmartClassroom/ # Django Base Project Folder. Auto-generated by Django-admin.
│   │   ├── __pycache__/
│   │   │   └── *.pyc
│   │   │
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── static_src/ # Known as static source files. Those are used for rendering of styles and used for extra functionalities of the web-app itself.
│   │   └── css/
│   │   │   └── *.css / *.css.map
│   │   │
│   │   └── js/
│   │   │   └── *.js / *.min.js / *.js.map
│   │   │
│   │   └── rsrc/
│   │       └── *.jpg / *.png
│   │
│   ├── template_CALLABLE/ # Known as Preset Components. Those are callables and referrable to Class-Basediews.
│   │   ├── elem_inst_view.html
│   │   └── *noContextReponseOnly.html
│   │
│   ├── template_REQUIRE/ # Known as Modular Components. Those are Required Templates To Use by the template_CALLABLE HTML Candidates.
│   │   ├── footer.html
│   │   ├── header.html
│   │   ├── modals.html
│   │   ├── nav.html
│   │   └── sidebar.html
│   │
│   ├── template_REUSE/ # Known as Reusable Components. Those templates have it's own content and cannot be paired with another reusable component.
│   │   ├── 404.html
│   │   ├── classroom_control.html
│   │   ├── dashboard.html
│   │   ├── instance_listviewer.html
│   │   └── login.html
│   │
│   ├── usersrc/ # Contents that are user-generated. They will be used in rendering if provided by the user.
│   │   └── <Confidential...>
│   │
│   └── manage.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── SC_ScriptInst.py
```

## Requirements

In this section, we're going to talk in the software-side and hardware-side. This should be enough if you're willing to duplicate this project both physically and virtually working. Keep in mind that this will be a bit hectic. So take time if you're willing to do something about this project.

### Hardware-Side

This project is so expensive asf in the hardware stuff so that should be a spoiler alert for you. It took our allowance by 75% by the time we're buying the components.

#### Microcontroller

#### Components

## Software-Side

### Deployment

In this section, we're going to talk about how to deploy this project. Unfortunately, we were able to deploy this project by Computer. We're supposed to deploy it in Raspberry Pi 4B but that didn't happened due to the pandemic.

`Coming Soon.`

If you're trying to make things and things doesn't go well. Please check the videos from the Demo and Resources Section. Which is located just belo!

## Demo and Resources

This section should be enough to know on what you're dealing in this project.

- Documentation: <https://docs.google.com/document/d/1oyZ-jKiQFd_voRn4EIxYd09oBhy7ZOXVMwA2KruXPwU/edit>
- Youtube Video Demonstration: <https://www.youtube.com/watch?v=jpxtz1-mhd8>
- Youtube Video Installation: <https://www.youtube.com/watch?v=1NmTDPHD-Js>

## 💁 ❔ Frequently Asked Questions

- I feel that some parts of this project is missing... Can you tell me what is it?
  - ***Sure bro...*** There are only a few things that are ****NOT CONSIDERED**** to give away. And those are the following:
    1. PCB Design
    2. Miniature Design Layout

- ***Your code is not that very much clean / My eyes hurt! / Why would you code something much inlined and quite... stupid???***
  - All codes that were done initially was not intended to be dirty as possible. They were like that due to the fact that we have deadlines to meet. That's because I did most of the work here (In Software-Side) for 3 months straight. So I apologize for such a messy code. And yeah, the hardest part to accept when making this one is that I was still learning the necessity parts of Django to our projects.

- ***Can I use this whenever I want?***
  - Yeah, sure. But keep note that the repository has a `GPL-3.0` license. You have to read it and understand why I have to choose this one.

- ***Do I really have to meet the required components indicated here?***
  - For compatibility, of course. Since I didn't provide for the schematics, you could use different components or MCUs to your liking.

- ***How did you come with this project?***
  - Long story short, I wanted to achieve ideal time for what allocated time was for the discussions and for the waiting time to open the room. In our school, you need a staff / administrator to open the room door for you. And I as for what I know, I don't like how we wasting our time for nothing. That's because they are late as usual. One thing to mention is that we have one course-dedicated room from the technological building and the one who is assigned to that building is taking a while to open our room because he was always **LATE**, and that is always the scenario during monday, wednesday, and friday. It makes me feel bad, the fact that building is highly focused on technology! So, to make atleast a solution, we were able to think of this project, without actually us thinking on how hard it is gonna be. And with that, few weeks later, this project was born.

- ***Why did you open-sourced this!? And aren't you afraid it as the Lead Developer?***
  - I don't want to put any of my works in the bookshelf from which other people doesn't see it. I want things to be accessible because that makes me want to value the hardworks and sleepless nights that I throw off especially on this project. And yes, I'm not afraid of getting stolen. I always assume we could do things legal and proper. And I'm already a victim of it and know how it feels to get stolen by someone else.

- ***What would you do if someone got **stonks** from this project?***
  - I might close this one down. But I believe this project is very hard to replicate physically. I just do hope I could get something on it, or even just credits were just fine. Keep in mind that the project is just a ***bare-minimum*** setup that could be possibly done in home or from small-scale buildings with multiple rooms. I know this type of setup is possibly expensive, but we're just showing here the concept of what IoT can do nowadays.

- ***Can I submit issues and submit proposal for alternative methods?***
  - That's a nice of you! Yes you can, just make things a bit formal. Even though I don't have a template for making it descent and formal as possible. I would just give you freedom on how would you laid out the proposals or issue. Just label things out accordingly in my labels that I made.

- ***This was such a medium-scale project!? How did you survive working on this one alone???***
  - I don't even know how I were able to survive this while learning throughout the semester. But hey, at least I wasn't suicidal or didn't got grave inside of a depression. But to be honest, I did survive by just literally working on it **non-stop**. You really have to sacrafice having fun and being go-happy with others. You really have to focus on it. Which in the end, **I was now quite emotionless, not being able to be happy at things that I want to be happy.** - ***DISCLAIMER - I'm not scaring you or other people at trying to sacrafice for the better, this was literally just happened due to circumstances. Maybe there's a better way to code productively and not by just coding all times and ending up at being emotionless and blame self for such stupid reasons...***

- ***Can I ask question/s?***
  - Sure thing! Just be polite and I'll answer your question through my email indicated in my Github Profile!

## 🏆 ✍ Authors

Here are the list of authors who is taking part of the project.

- **Embedded Systems Team**
  - **Janrey Licas** - *Initial Work / Project Lead / Overall Software Design Worker / FrontEnd Design and Backend Programming* -  [CodexLink](https://github.com/CodexLink)
  - **Janos Angelo Garcia Jantoc** - *Hardware PCB Designer and Post Project Worker* - [BigBossCodes](https://github.com/BigBossCodes)
  - **Johnell Casey Murillo Panotes** - *The Participant and Initial Bare Minimum Documentation Worker* - No Account

- **Internet of Thing Team**
  - **Janrey Licas** - *Initial Work / Project Lead / Overall Software Design Worker / FrontEnd Design and Backend Programming* -  [CodexLink](https://github.com/CodexLink)
  - **Janos Angelo Garcia Jantoc** - *Hardware PCB Designer and Post Project Worker* - [BigBossCodes](https://github.com/BigBossCodes)
  - **Ronald Langaoan Jr.** - *Hardware Designer and Miniature Builder*[AliasBangis](https://github.com/AliasBangis)
  - **Joshua Santos** - *Initial Build Supporter and Joint Project Leader from Logic Circuits and Design* - No Account


## 📜 Credits

- Personals

- Libraries


## 📚 License

This project is licensed under the GNU v3 License - see the [LICENSE](https://github.com/CodexLink/SmartClassroomSystem/blob/master/LICENSE) file for details
