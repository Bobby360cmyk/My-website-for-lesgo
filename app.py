from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>A Question For You</title>
    <style>
        :root {
            --bg1: #fff1f5;
            --bg2: #ffe4ec;
            --card: rgba(255, 255, 255, 0.92);
            --text: #2f2a2c;
            --muted: #6d5f66;
            --accent: #ff4f87;
            --accent-dark: #e63f76;
            --soft: #ffd7e4;
            --shadow: 0 12px 35px rgba(0, 0, 0, 0.12);
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, Helvetica, sans-serif;
            color: var(--text);
            background:
                radial-gradient(circle at top left, #ffffff 0%, transparent 30%),
                linear-gradient(135deg, var(--bg1), var(--bg2));
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 18px;
            overflow-x: hidden;
        }

        .floating-hearts {
            position: fixed;
            inset: 0;
            pointer-events: none;
            overflow: hidden;
        }

        .heart {
            position: absolute;
            bottom: -40px;
            font-size: 20px;
            opacity: 0.18;
            animation: floatUp linear infinite;
        }

        .heart:nth-child(1) { left: 8%; animation-duration: 10s; }
        .heart:nth-child(2) { left: 22%; animation-duration: 13s; font-size: 16px; }
        .heart:nth-child(3) { left: 37%; animation-duration: 11s; }
        .heart:nth-child(4) { left: 52%; animation-duration: 15s; font-size: 24px; }
        .heart:nth-child(5) { left: 68%; animation-duration: 12s; }
        .heart:nth-child(6) { left: 83%; animation-duration: 14s; font-size: 18px; }

        @keyframes floatUp {
            0% {
                transform: translateY(0) scale(1);
                opacity: 0;
            }
            10% {
                opacity: 0.18;
            }
            100% {
                transform: translateY(-115vh) scale(1.2);
                opacity: 0;
            }
        }

        .card {
            width: 100%;
            max-width: 460px;
            background: var(--card);
            backdrop-filter: blur(8px);
            border-radius: 26px;
            box-shadow: var(--shadow);
            padding: 28px 22px;
            text-align: center;
            position: relative;
            z-index: 2;
        }

        .badge {
            display: inline-block;
            background: #fff;
            color: var(--accent-dark);
            border: 1px solid #ffd0df;
            padding: 8px 14px;
            border-radius: 999px;
            font-size: 0.9rem;
            margin-bottom: 14px;
            box-shadow: 0 4px 12px rgba(255, 79, 135, 0.08);
        }

        h1 {
            margin: 0 0 10px;
            font-size: 2rem;
            line-height: 1.15;
        }

        .subtitle {
            margin: 0 auto 18px;
            max-width: 320px;
            color: var(--muted);
            line-height: 1.5;
            font-size: 1rem;
        }

        .message-box {
            background: linear-gradient(180deg, #fff9fb, #fff1f5);
            border: 1px solid #ffdce8;
            border-radius: 20px;
            padding: 18px;
            margin: 20px 0;
            text-align: left;
            line-height: 1.7;
            font-size: 1rem;
        }

        .question {
            margin-top: 12px;
            text-align: center;
            font-size: 1.15rem;
            font-weight: bold;
            color: var(--accent-dark);
        }

        .buttons {
            position: relative;
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-top: 22px;
            flex-wrap: wrap;
            min-height: 58px;
        }

        button {
            border: none;
            border-radius: 999px;
            padding: 14px 24px;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
            min-width: 130px;
        }

        button:hover {
            transform: translateY(-2px);
        }

        .yes-btn {
            background: var(--accent);
            color: white;
            box-shadow: 0 10px 18px rgba(255, 79, 135, 0.24);
        }

        .yes-btn:hover {
            background: var(--accent-dark);
        }

        .no-btn {
            background: white;
            color: #555;
            border: 1px solid #eee;
            position: relative;
        }

        .result {
            margin-top: 20px;
            min-height: 28px;
            font-size: 1.05rem;
            font-weight: bold;
            color: var(--accent-dark);
        }

        .final-screen {
            display: none;
            animation: fadeIn 0.5s ease;
        }

        .celebrate {
            font-size: 3rem;
            margin-bottom: 10px;
        }

        .footer {
            margin-top: 18px;
            color: #8b7d84;
            font-size: 0.9rem;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 520px) {
            .card {
                padding: 24px 16px;
                border-radius: 22px;
            }

            h1 {
                font-size: 1.7rem;
            }

            .subtitle,
            .message-box,
            .result {
                font-size: 0.97rem;
            }

            .buttons {
                flex-direction: column;
                align-items: center;
            }

            button {
                width: 100%;
                max-width: 280px;
            }
        }
    </style>
</head>
<body>
    <div class="floating-hearts">
        <div class="heart">❤</div>
        <div class="heart">❤</div>
        <div class="heart">❤</div>
        <div class="heart">❤</div>
        <div class="heart">❤</div>
        <div class="heart">❤</div>
    </div>

    <div class="card" id="mainCard">
        <div id="questionScreen">
            <div class="badge">A little something for you</div>
            <h1>Hey, Lesego</h1>
            <p class="subtitle">
                I wanted to ask you something in a way that felt thoughtful and special.
            </p>

            <div class="message-box">
                Getting to know you has honestly made me really happy.
                I love the time we spend together, and you always make things feel lighter and better.
                <br><br>
                So instead of just sending a normal message, I wanted to do this properly.
                <div class="question">Will you be my girlfriend?</div>
            </div>

            <div class="buttons" id="buttonArea">
                <button class="yes-btn" onclick="showYes()">Yes 💖</button>
                <button class="no-btn" id="noBtn" onmouseover="moveNoButton()" onclick="moveNoButton()">No 🙈</button>
            </div>

            <div class="result" id="result"></div>
            <div class="footer">Made with care.</div>
        </div>

        <div class="final-screen" id="finalScreen">
            <div class="celebrate">🎉💖</div>
            <h1>You just made my whole day</h1>
            <p class="subtitle" style="max-width: 340px;">
                Thank you for saying yes. This means a lot to me, and I’m really excited for us.
            </p>
            <div class="message-box" style="text-align:center;">
                You are officially my favorite person to make websites for.
            </div>
            <div class="footer">Best answer ever.</div>
        </div>
    </div>

    <script>
        let noMoves = 0;

        function showYes() {
            document.getElementById("questionScreen").style.display = "none";
            document.getElementById("finalScreen").style.display = "block";
            createConfetti();
        }

        function moveNoButton() {
            const button = document.getElementById("noBtn");
            const area = document.getElementById("buttonArea");

            if (window.innerWidth <= 520) {
                const messages = [
                    "Are you sure? 😅",
                    "Maybe give the other button a chance 👀",
                    "That one is clearly the better option 💕"
                ];
                document.getElementById("result").innerText = messages[noMoves % messages.length];
                noMoves++;
                return;
            }

            const maxX = area.offsetWidth / 2 - 70;
            const x = Math.floor(Math.random() * (maxX * 2)) - maxX;
            const y = Math.floor(Math.random() * 30) - 10;

            button.style.transform = `translate(${x}px, ${y}px)`;

            const messages = [
                "Hmm... try the pink one 😄",
                "That button is a little shy today 🙈",
                "I think the 'Yes' button looks better 💖"
            ];
            document.getElementById("result").innerText = messages[noMoves % messages.length];
            noMoves++;
        }

        function createConfetti() {
            for (let i = 0; i < 28; i++) {
                const piece = document.createElement("div");
                piece.innerHTML = ["💖", "✨", "🎉", "💕"][Math.floor(Math.random() * 4)];
                piece.style.position = "fixed";
                piece.style.left = Math.random() * 100 + "vw";
                piece.style.top = "-30px";
                piece.style.fontSize = (18 + Math.random() * 14) + "px";
                piece.style.zIndex = "9999";
                piece.style.pointerEvents = "none";
                piece.style.transition = "transform 2.8s linear, top 2.8s linear, opacity 2.8s ease";
                document.body.appendChild(piece);

                setTimeout(() => {
                    piece.style.top = "100vh";
                    piece.style.transform = `translateX(${(Math.random() - 0.5) * 120}px) rotate(${Math.random() * 360}deg)`;
                    piece.style.opacity = "0";
                }, 50);

                setTimeout(() => {
                    piece.remove();
                }, 3000);
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, )