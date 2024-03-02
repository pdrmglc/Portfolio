SELECT P.nome AS "Nome do Paciente", P.data_nascimento AS "Data de nascimento", P.sexo AS "Sexo", A.id_amostra AS "Codigo da amostra", A.data_coleta AS "Data de coleta da amostra", A.estado_coleta AS "Estado de coleta da amostra"
FROM Pacientes P
JOIN Amostras A ON P.id_paciente = A.id_paciente
WHERE P.sexo = "M";