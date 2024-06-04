import streamlit as st
import pandas as pd
import numpy as np
import pickle
from operator import itemgetter
import sklearn

st.set_page_config(page_icon="https://app.dadosfera.ai/pt-BR/favicon.ico", page_title="Dadosfera - Simulador")

# Código CSS para alterar a cor da barra lateral
css = """
    <style>
    body {
        margin: 0;
        padding: 0;
        background-color: #f2f2f2;
    }
    .container {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    img {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 300px;
        height: 300px;
    }
    </style>
    """

# Injetar o código CSS no app
st.markdown(css, unsafe_allow_html=True)

# Cria um contêiner para centralizar a imagem
with st.container():
    # Insere a imagem
    st.image("https://app.dadosfera.ai/en-US/assets/images/identity/dadosfera-login.svg", width=150)


# Carregar variáveis do arquivo pickle
with open('treinados.pkl', 'rb') as f:
    data = pickle.load(f)
gb = data['gb']

with open('model.pkl', 'rb') as f:
    data = pickle.load(f)
model_db = data['model_db']

with open('stats.pkl', 'rb') as f:
    data = pickle.load(f)
team_stats_raw = data['team_stats_raw']

# Dados
table = {
    'A': [['Argentina', 0, []], ['Peru', 0, []], ['Chile', 0, []], ['Canada', 0, []]],
    'B': [['Mexico', 0, []], ['Ecuador', 0, []], ['Venezuela', 0, []], ['Jamaica', 0, []]],
    'C': [['United States', 0, []], ['Uruguay', 0, []], ['Panama', 0, []], ['Bolivia', 0, []]],
    'D': [['Brazil', 0, []], ['Colombia', 0, []], ['Paraguay', 0, []], ['Costa Rica', 0, []]]
}

matches = [
    ('A', 'Argentina', 'Canada'), ('A', 'Peru', 'Chile'), ('A', 'Peru', 'Canada'),
    ('A', 'Chile', 'Argentina'), ('A', 'Argentina', 'Peru'), ('A', 'Canada', 'Chile'),
    ('B', 'Ecuador', 'Venezuela'), ('B', 'Mexico', 'Jamaica'), ('B', 'Ecuador', 'Jamaica'),
    ('B', 'Venezuela', 'Mexico'), ('B', 'Mexico', 'Ecuador'), ('B', 'Jamaica', 'Venezuela'),
    ('C', 'United States', 'Bolivia'), ('C', 'Uruguay', 'Panama'), ('C', 'Panama', 'United States'),
    ('C', 'Uruguay', 'Bolivia'), ('C', 'United States', 'Uruguay'), ('C', 'Bolivia', 'Panama'),
    ('D', 'Colombia', 'Paraguay'), ('D', 'Brazil', 'Costa Rica'), ('D', 'Colombia', 'Costa Rica'),
    ('D', 'Paraguay', 'Brazil'), ('D', 'Brazil', 'Colombia'), ('D', 'Costa Rica', 'Paraguay')
]

# Função para encontrar as estatísticas da equipe
def find_stats(team_1):
    past_games = team_stats_raw[team_stats_raw["team"] == team_1].sort_values("date")
    last5 = past_games.tail(5)

    team_1_rank = past_games["rank"].values[-1]
    team_1_goals = past_games.score.mean()
    team_1_goals_l5 = last5.score.mean()
    team_1_goals_suf = past_games.suf_score.mean()
    team_1_goals_suf_l5 = last5.suf_score.mean()
    team_1_rank_suf = past_games.rank_suf.mean()
    team_1_rank_suf_l5 = last5.rank_suf.mean()
    team_1_gp_rank = past_games.points_by_rank.mean()
    team_1_gp_rank_l5 = last5.points_by_rank.mean()

    return [team_1_rank, team_1_goals, team_1_goals_l5, team_1_goals_suf, team_1_goals_suf_l5, team_1_rank_suf, team_1_rank_suf_l5, team_1_gp_rank, team_1_gp_rank_l5]

# Função para encontrar as características da equipe
def find_features(team_1, team_2):
    rank_dif = team_1[0] - team_2[0]
    goals_dif = team_1[1] - team_2[1]
    goals_dif_l5 = team_1[2] - team_2[2]
    goals_suf_dif = team_1[3] - team_2[3]
    goals_suf_dif_l5 = team_1[4] - team_2[4]
    goals_per_ranking_dif = (team_1[1] / team_1[5]) - (team_2[1] / team_2[5])
    dif_rank_agst = team_1[5] - team_2[5]
    dif_rank_agst_l5 = team_1[6] - team_2[6]
    dif_gp_rank = team_1[7] - team_2[7]
    dif_gp_rank_l5 = team_1[8] - team_2[8]

    return [rank_dif, goals_dif, goals_dif_l5, goals_suf_dif, goals_suf_dif_l5, goals_per_ranking_dif, dif_rank_agst, dif_rank_agst_l5, dif_gp_rank, dif_gp_rank_l5, 1, 0]

# Função para exibir os grupos
def show_groups(groups):
    for group, teams in groups.items():
        st.write(f"## Grupo {group}")
        df = pd.DataFrame(teams, columns=["Equipe", "Pontos", "Partidas"])
        df = df.sort_values(by="Pontos", ascending=False)  # Ordena os dados por pontos em ordem decrescente
        st.table(df.drop(columns=["Pontos", "Partidas"]))

def show_groups_poin(groups):
    for group, teams in groups.items():
        st.write(f"## Grupo {group}")
        df = pd.DataFrame(teams, columns=["Equipe", "Pontos", "Partidas"])
        df = df.sort_values(by="Pontos", ascending=False)  # Ordena os dados por pontos em ordem decrescente
        st.table(df.drop(columns=["Partidas"]))

# Função para simular jogos e atualizar a tabela
def simulate_and_update_table(table, matches):
    last_group = ""
    advanced_group = []

    for teams in matches:
        draw = False
        team_1 = find_stats(teams[1])
        team_2 = find_stats(teams[2])

        features_g1 = find_features(team_1, team_2)
        features_g2 = find_features(team_2, team_1)

        probs_g1 = gb.predict_proba([features_g1])
        probs_g2 = gb.predict_proba([features_g2])

        team_1_prob_g1 = probs_g1[0][0]
        team_1_prob_g2 = probs_g2[0][1]
        team_2_prob_g1 = probs_g1[0][1]
        team_2_prob_g2 = probs_g2[0][0]

        team_1_prob = (team_1_prob_g1 + team_1_prob_g2) / 2
        team_2_prob = (team_2_prob_g1 + team_2_prob_g2) / 2

        if (
            (team_1_prob_g1 > team_2_prob_g1)
            & (team_2_prob_g2 > team_1_prob_g2)
            or ((team_1_prob_g1 < team_2_prob_g1) & (team_2_prob_g2 < team_1_prob_g2))
        ):
            draw = True
            for i in table[teams[0]]:
                if i[0] == teams[1] or i[0] == teams[2]:
                    i[1] += 1
        elif team_1_prob > team_2_prob:
            winner = teams[1]
            for i in table[teams[0]]:
                if i[0] == teams[1]:
                    i[1] += 3
        else:
            winner = teams[2]
            for i in table[teams[0]]:
                if i[0] == teams[2]:
                    i[1] += 3

        for i in table[teams[0]]:
            if i[0] == teams[1]:
                i[2].append(team_1_prob)
            if i[0] == teams[2]:
                i[2].append(team_2_prob)

        if last_group != teams[0]:
            if last_group != "":
                for i in table[last_group]:
                    i[2] = np.mean(i[2])
                final_points = table[last_group]
                final_table = sorted(final_points, key=itemgetter(1, 2), reverse=True)
                advanced_group.append([final_table[0][0], final_table[1][0]])

            if not draw:
                pass
                # st.write(f"Grupo {teams[0]} - {teams[1]} vs. {teams[2]}: Vencedor {winner} com {max(team_1_prob, team_2_prob):.2f} de probabilidade")
            else:
                pass
                # st.write(f"Grupo {teams[0]} - {teams[1]} vs. {teams[2]}: Empate")
        last_group = teams[0]

    for i in table[last_group]:
        i[2] = np.mean(i[2])
    final_points = table[last_group]
    final_table = sorted(final_points, key=itemgetter(1, 2), reverse=True)
    advanced_group.append([final_table[0][0], final_table[1][0]])

    return advanced_group

# Função para simular os playoffs
# Função para simular os playoffs
def simulate_playoffs(advanced_group):
    playoffs = {"Quartas de Final": [], "Semi-Final": [], "Final": []}

    # Definir os confrontos das Quartas de Final
    playoffs["Quartas de Final"] = [
        [advanced_group[0][0], advanced_group[1][1]],  # 1A vs 2B
        [advanced_group[0][1], advanced_group[1][0]],  # 2A vs 1B
        [advanced_group[2][0], advanced_group[3][1]],  # 1C vs 2D
        [advanced_group[2][1], advanced_group[3][0]]   # 2C vs 1D
    ]

    next_rounds = []
    actual_round = ""

    for p in playoffs.keys():
        next_rounds = []
        for game in playoffs[p]:
            home = game[0]
            away = game[1]
            team_1 = find_stats(home)
            team_2 = find_stats(away)

            features_g1 = find_features(team_1, team_2)
            features_g2 = find_features(team_2, team_1)

            probs_g1 = gb.predict_proba([features_g1])
            probs_g2 = gb.predict_proba([features_g2])

            team_1_prob = (probs_g1[0][0] + probs_g2[0][1]) / 2
            team_2_prob = (probs_g2[0][0] + probs_g1[0][1]) / 2

            if actual_round != p:
                st.write("-" * 10)
                st.write(f"**{p}**")
                st.write("-" * 10)
                st.write("\n")

            st.write(f"{home} vs. {away}")
            progress_bar = st.progress(0)

            for i in range(100):
                progress_bar.progress(i + 1)

            if team_1_prob < team_2_prob:
                st.write(f"{away} avança com a probabilidade de **{team_2_prob:.2f}**")
                next_rounds.append(away)
            else:
                st.write(f"{home} avança com a probabilidade de **{team_1_prob:.2f}**")
                next_rounds.append(home)

            game.append([team_1_prob, team_2_prob])
            actual_round = p

        if p == "Quartas de Final":
            playoffs["Semi-Final"] = [[next_rounds[i], next_rounds[i + 1]] for i in range(0, len(next_rounds) - 1, 2)]
        elif p == "Semi-Final":
            playoffs["Final"] = [[next_rounds[0], next_rounds[1]]]

    final_game = playoffs["Final"][0]
    home = final_game[0]
    away = final_game[1]
    team_1 = find_stats(home)
    team_2 = find_stats(away)

    features_g1 = find_features(team_1, team_2)
    features_g2 = find_features(team_2, team_1)

    probs_g1 = gb.predict_proba([features_g1])
    probs_g2 = gb.predict_proba([features_g2])

    team_1_prob = (probs_g1[0][0] + probs_g2[0][1]) / 2
    team_2_prob = (probs_g2[0][0] + probs_g1[0][1]) / 2

# Interface do Streamlit

st.markdown("<h1 style='margin-top: 100px;'>Simulador Copa América 2024</h1>", unsafe_allow_html=True)

show_groups(table)

if st.button('Simular Jogos'):
    advanced_group = simulate_and_update_table(table, matches)
    st.write("## Resultados Atualizados dos Grupos")
    show_groups_poin(table)
    st.write("## Simulação dos Playoffs")
    simulate_playoffs(advanced_group)