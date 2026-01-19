import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

print("🚀 Avvio analisi strategica...")

# 1. Controllo file dati
path = 'data/insurance_market_data.csv'
if os.path.exists(path):
    df = pd.read_csv(path)
    print(f"✅ Dati caricati correttamente: {len(df)} righe trovate.")
else:
    print(f"❌ Errore: Non trovo il file in {path}")
    exit()

# 2. Simulazione Business Case
revenue = 1000 * 0.10 * 600
print(f"💰 ROI Stimato: €{revenue:,}")

# 3. Creazione Grafici
print("📊 Generazione grafici in corso...")
plt.figure(figsize=(10,6))
sns.barplot(data=df, x='Region', y='Annual_OOP_Spending', ci=None)
plt.title('Protection Gap by Region')

# Salvataggio forzato (così non dobbiamo sperare che si apra la finestra)
output_path = 'strategic_chart.png'
plt.savefig(output_path)
print(f"✅ Grafico salvato come immagine: {output_path}")
print("🏁 Analisi completata!")