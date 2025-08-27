import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV oku
df = pd.read_csv("premier_league_stats_2024-25.csv")
df['xG_diff'] = df['GF'] - df['xG']

# Grafik stilini ayarla
sns.set_theme(style="whitegrid")

# 1. Puan Tablosu (ilk 5)
top_points = df[['Squad', 'Pts']].sort_values(by='Pts', ascending=False).head(5)
plt.figure(figsize=(8,5))
sns.barplot(data=top_points, x="Pts", y="Squad", palette="viridis")
plt.title("🔝 En Çok Puan Toplayan İlk 5 Takım")
plt.xlabel("Puan")
plt.ylabel("Takım")
plt.show()

# 2. En çok gol atan takım
plt.figure(figsize=(8,5))
sns.barplot(data=df.sort_values(by="GF", ascending=False).head(5),
            x="GF", y="Squad", palette="magma")
plt.title("⚽ En Çok Gol Atan İlk 5 Takım")
plt.xlabel("Gol Sayısı")
plt.ylabel("Takım")
plt.show()

# 3. En az gol yiyen takım
plt.figure(figsize=(8,5))
sns.barplot(data=df.sort_values(by="GA", ascending=True).head(5),
            x="GA", y="Squad", palette="Blues_r")
plt.title("🛡️ En Az Gol Yiyen İlk 5 Takım")
plt.xlabel("Yenilen Gol")
plt.ylabel("Takım")
plt.show()

# 4. Beklenenden iyi/kötü oynayanlar (GF - xG)
plt.figure(figsize=(10,6))
sorted_diff = df.sort_values(by="xG_diff", ascending=False)
sns.barplot(data=sorted_diff, x="xG_diff", y="Squad", palette="coolwarm")
plt.axvline(0, color="black", linestyle="--")
plt.title("📊 Takımların Beklenen Gol (xG) ile Gerçek Gol Farkı")
plt.xlabel("Gerçek Gol - xG")
plt.ylabel("Takım")
plt.show()

# 5. Seyirci ortalaması
plt.figure(figsize=(8,5))
attendance_top = df[['Squad', 'Attendance']].sort_values(by='Attendance', ascending=False).head(5)
sns.barplot(data=attendance_top, x="Attendance", y="Squad", palette="cividis")
plt.title("🏟️ En Yüksek Seyirci Ortalaması (İlk 5)")
plt.xlabel("Ortalama Seyirci")
plt.ylabel("Takım")
plt.show()
