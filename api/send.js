export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { message } = req.body;

    const webhookURL = "https://canary.discord.com/api/webhooks/1376130665996750919/nmVIx9xvrzDKoVs8zs22g3GwG05Xi38ejIl77nEI9xjsQYezC-pU8qNLo2u-HgCM9s2B";

    const response = await fetch(webhookURL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ content: message }),
    });

    if (response.ok) {
      res.status(200).json({ success: true });
    } else {
      res.status(500).json({ success: false });
    }
  } else {
    res.status(405).json({ error: "Method not allowed" });
  }
}

export const config = {
  api: {
    bodyParser: true,
  },
};
