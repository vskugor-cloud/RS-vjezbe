   import express from "express";

   const app = express();
   app.use(express.json());

   const PORT = process.env.PORT || 3000;

   // Podaci su u memoriji, pa se resetiraju pri svakom ponovnom pokretanju servera
   let items = [{ id: 1, name: "Prvi zadatak" }];
   let nextId = 2;

   app.get("/api/health", (req, res) => {
     res.json({ status: "ok" });
   });

   app.get("/api/items", (req, res) => {
     res.json(items);
   });

   app.get("/api/items/:id", (req, res) => {
     const item = items.find((i) => i.id === Number(req.params.id));
     if (!item) {
       return res.status(404).json({ error: "Stavka nije pronađena" });
     }
     res.json(item);
   });

   app.post("/api/items", (req, res) => {
     const { name } = req.body;
     if (!name) {
       return res.status(400).json({ error: "Polje 'name' je obavezno" });
     }
     const item = { id: nextId++, name };
     items.push(item);
     res.status(201).json(item);
   });

   app.delete("/api/items/:id", (req, res) => {
     const index = items.findIndex((i) => i.id === Number(req.params.id));
     if (index === -1) {
       return res.status(404).json({ error: "Stavka nije pronađena" });
     }
     items.splice(index, 1);
     res.status(204).end();
   });

   app.listen(PORT, "0.0.0.0", () => {
     console.log(`Server radi na portu ${PORT}`);
   });