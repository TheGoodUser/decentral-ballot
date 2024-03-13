# Get Started with [DecentralBallot](https://github.com/TheGoodUser/decentral-ballot-CODEMATRIX-)

Welcome to **DecentralBallot** - your gateway to a revolutionary blockchain-based voting experience! 🚀

## What is DecentralBallot?

DecentralBallot is not just another voting platform; it's a cutting-edge, decentralized democracy tool designed to redefine the way you participate in elections. Say goodbye to traditional voting booths and embrace the future of remote voting.

## Why DecentralBallot?

🌐 **Vote from Anywhere:** Exercise your democratic right from the comfort of your own home, office, or wherever you are in the world.

💼 **Candidate Eligibility:** Only verified candidates are included in the platform, ensuring that your vote counts towards credible and legitimate individuals.

💽 **Efficient Storage:** We've optimized the platform to record votes as compact binary blocks, guaranteeing minimal storage consumption without compromising data integrity.

## How it Works

- **Files:**
  - `Server.py`: The main server file which connects through the other nodes using websockets on LAN.
  - `blockchain.py`: This program creates genesis and other new blocks for every vote.
  - `index.html`: The main window from which you can vote. First your identity is confirmed through the database and then the voting panel is enabled.

- **Blockchain Magic:** Each vote is recorded as a block in our blockchain, ensuring a secure and tamper-proof voting process. The blocks are recorded in the format:-
  -  ```
     { 
        "index": 0,
        "previous_hash": "0",
        "timestamp": 1710223857.9971855,
        "vote_for": "Genesis Vote",
        "hash": "849fb6e88d29d27e26accbd0b3cab19ca6944f49f7b0215947e4333910f9693f"
     }
     ```
  
- **Real-Time Transparency:** Witness the power of decentralized democracy with real-time updates. As votes are cast, blocks are added to the blockchain, providing a live display of the voting action.



## Get Started Now!

Ready to embark on a journey of safe, secure, and transparent voting? Follow these simple steps:

1. **Visit DecentralBallot Repository:** [DecentralBallot GitHub](https://github.com/TheGoodUser/decentral-ballot-CODEMATRIX-)

2. **Explore the Code:** Dive into the heart of DecentralBallot's open-source code. Feel free to contribute and be part of the democratic revolution!

3. **Issues and Feedback:** Have ideas or feedback? Share them in the repository's issues section. Your input is crucial to shaping the future of decentralized voting.

4. **Spread the Word:** Help us spread the word about DecentralBallot. The more voices, the stronger the current of change!

Ready to cast your digital ballot? Let DecentralBallot guide you to a new era of democratic participation. 🗳️💻
