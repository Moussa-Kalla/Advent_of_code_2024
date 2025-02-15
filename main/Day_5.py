from collections import defaultdict, deque

class Day_5:
    def __init__(self, fichier):
        self.fichier = fichier
        self.liste_regles, self.liste_ms_a_j = self._lecture_fichier_txt()

    def _lecture_fichier_txt(self):
        with open(self.fichier, 'r') as fichier:
            lignes = fichier.readlines()

        regles = []
        ms_a_j = []
        en_mode_ms_a_j = False

        for ligne in lignes:
            ligne = ligne.strip()
            if not ligne:
                en_mode_ms_a_j = True
                continue
            if en_mode_ms_a_j:
                ms_a_j.append(list(map(int, ligne.split(','))))
            else:
                regles.append(list(map(int, ligne.split('|'))))
        return regles, ms_a_j

    def _const_graphe(self, liste_regles):
        graphe = defaultdict(list)
        for origine, destination in liste_regles:
            graphe[origine].append(destination)
        return graphe

    def _m_a_j_valide(self, m_a_j, graphe):
        index_page = {page: i for i, page in enumerate(m_a_j)}
        for origine, destinations in graphe.items():
            if origine in index_page:
                for destination in destinations:
                    if destination in index_page and index_page[origine] > index_page[destination]:
                        return False
        return True

    def _trouver_page_milieu(self, m_a_j):
        index_milieu = len(m_a_j) // 2
        return m_a_j[index_milieu]

    def partie_1(self):
        graphe = self._const_graphe(self.liste_regles)
        ms_a_j_valides = [m_a_j for m_a_j in self.liste_ms_a_j if self._m_a_j_valide(m_a_j, graphe)]
        return sum(self._trouver_page_milieu(m_a_j) for m_a_j in ms_a_j_valides)

    def _tri_topologique(self, m_a_j, graphe):
        degre_ent = defaultdict(int)
        liste_adj = defaultdict(list)
        ens_m_a_j = set(m_a_j)

        for x in ens_m_a_j:
            for y in graphe.get(x, []):
                if y in ens_m_a_j:
                    liste_adj[x].append(y)
                    degre_ent[y] += 1

        file = deque([x for x in ens_m_a_j if degre_ent[x] == 0])
        m_a_j_triee = []

        while file:
            courant = file.popleft()
            m_a_j_triee.append(courant)
            for voisin in liste_adj[courant]:
                degre_ent[voisin] -= 1
                if degre_ent[voisin] == 0:
                    file.append(voisin)
        return m_a_j_triee

    def partie_2(self):
        graphe = self._const_graphe(self.liste_regles)
        ms_a_j_incorrectes = [m_a_j for m_a_j in self.liste_ms_a_j if not self._m_a_j_valide(m_a_j, graphe)]
        ms_a_j_corrigees = [self._tri_topologique(m_a_j, graphe) for m_a_j in ms_a_j_incorrectes]
        return sum(self._trouver_page_milieu(m_a_j) for m_a_j in ms_a_j_corrigees)

if __name__ == "__main__":
    lien_fichier = "Input_Data/Day_5.txt"
    calculateur = Day_5(lien_fichier)
    
    print(calculateur.partie_1())
    print(calculateur.partie_2())