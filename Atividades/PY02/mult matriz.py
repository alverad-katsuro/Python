def sao_multiplicaveis(m1,m2):
    try:
        m1_l = len(m1)
        m2_c = len(m2[0])
        if m1_l <= m2_c:
            try:
                m2_l = len(m2)
                m1_c = len([0])
                if m2_l > m1_c:
                    return False
                else:
                    return True
            except TypeError:
                return True
        else:
            return False
    except TypeError:
        return False
sao_multiplicaveis(([1],[2],[3]),([1,2,3],[1,2,3]))