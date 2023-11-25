import matplotlib.pyplot as plt

# Datos
presidentes = ["Eduardo Duhalde", "Néstor Kirchner", "Cristina Fernández", "Cristina Fernández", "Mauricio Macri", "Alberto Fernández"]
reservas_brutas = [11045, 45811, 46371, 25030, 43797, 20928]
reservas_liquidas = [-5165, 39175, 31393, 6981, 10580, -16889]

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(presidentes))

bars1 = plt.bar(index, reservas_brutas, bar_width, label='Reservas Brutas')
bars2 = plt.bar([i + bar_width for i in index], reservas_liquidas, bar_width, label='Reservas Líquidas')

# Etiquetas con los valores de los datos en las barras
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval), ha='center', va='bottom')

# Etiquetas, título y leyenda
plt.xlabel('Presidentes')
plt.ylabel('Reservas en millones de USD')
plt.title('Reservas Brutas y Líquidas por Presidente')
plt.xticks([i + bar_width / 2 for i in index], presidentes, rotation=45)
plt.legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()
