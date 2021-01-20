def soma_matrizes(m1,m2):
    m1_l = len(m1)
    m2_l = len(m2)
    if m1_l == m2_l:
        try:
            try:
                m1_c = len(m1[0])
                m2_c = len(m2[0])
                if m1_c == m2_c:
                    pass
                else:
                    return False
            except TypeError:
                pass
            m3 = []
            try:
                if (m1_l == m2_l) and (m2_c == m1_c):
                    for i in range(m1_l):
                        m = []
                        for k in range(m1_c):
                            m.append((m1[i][k] + m2[i][k]))
                        m3.append(m)
                    return m3
            except UnboundLocalError:
                for i in range(m1_l):
                        m3.append(m1[i] + m2[i])
                return m3
        except ValueError:
            return False
    else:
        return False
