import matplotlib.pyplot as plt

# Dados filtrados (top 10)
top_users = {
    "Theoline Isaacson": 0.01477,
    "Jdhank": 0.01113,
    "Deplorable D": 0.01243,
    "besnook": 0.01085,
    "gregga777": 0.01061,
    "cognitive dissident": 0.01061,
    "KoJo": 0.01217,
    "Richard": 0.00788,
    "Rainman": 0.00496,
    "George Washington": 0.00540
}

plt.barh(list(top_users.keys()), list(top_users.values()), color='skyblue')
plt.xlabel('Score de PageRank')
plt.title('Top 10 Usuários Mais Influentes')
plt.gca().invert_yaxis()  # Ordenar do maior para o menor

plt.tight_layout()  # Evita corte de textos no eixo y
plt.savefig('top10_pagerank.png', dpi=300, bbox_inches='tight')  # Salvar imagem
plt.show()
