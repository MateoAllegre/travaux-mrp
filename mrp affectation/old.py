"""
def gale_shapley(n, agencies_choices, candidates_choices):
    # Dictionnaires pour stocker l'affectation
    agen_assi = {}
    cand_assi = {}

    # Copie pour préserver l'originale
    agen_choices = agencies_choices.copy()

    # Liste d'agences/candidats non liés par l'affectation
    list_free_agencies = list(agencies_choices.keys())
    list_free_candidates = list(candidates_choices.keys())

    while len(list_free_agencies) > 0: # Tant qu'il reste des agences libres

        agency = list_free_agencies[0] # Agence qu'on traite (parmi les libres)
        pot_cand = agen_choices[agency][0] # Candidat potentiel : choix favori de l'agence (parmi ceux qui restent)

        # CAS 1 : Candidat non lié
        if pot_cand in list_free_candidates:
            # On lie le candidat et l'agence ("de force")
            agen_assi[agency] = pot_cand
            cand_assi[pot_cand] = agency

            # le candidat et l'agence ne sont plus libres
            list_free_candidates.remove(pot_cand) 
            list_free_agencies.remove(agency)

        # CAS 2 : Candidat lié
        else:
            # Liste des choix du candidat potentiel
            pot_cand_ch = candidates_choices[pot_cand]

            # CAS 2a: le candidat préfère la nouvelle agence à la sienne
            if pot_cand_ch.index(agency) < pot_cand_ch.index(cand_assi[pot_cand]):
                # L'agence n'est plus libre mais l'ancienne agence du candidat le devient
                list_free_agencies.remove(agency)
                list_free_agencies.append(cand_assi[pot_cand])

                # L'ancienne agence n'est plus liée au candidat ("divorce")
                agen_assi.pop(cand_assi[pot_cand])

                # On lie le candidat et l'agence
                agen_assi[agency] = pot_cand
                cand_assi[pot_cand] = agency

            # CAS 2B: le candidat préférait son ancienne agence
            else:
                # Ce candidat ne convient pas, on le retire de la liste des choix de l'agence
                agen_choices[agency].remove(pot_cand)

    # On retourne les deux dictionnaires (i.e. l'affectation)
    return agen_assi, cand_assi 
"""