INSERT INTO Pacientes (id_paciente, nome, data_nascimento, sexo) VALUES
(1, 'João Silva', '1980-06-15', 'M'),
(2, 'Maria Oliveira', '1992-11-23', 'F'),
(3, 'Carlos Souza', '1975-03-30', 'M'),
(4, 'Ana Santos', '1988-09-10', 'F'),
(5, 'Pedro Costa', '2001-01-01', 'M');

INSERT INTO Hospitais (id_hospital, endereco) VALUES
(1, 'Rua A, 123, Cidade X'),
(2, 'Rua B, 456, Cidade Y'),
(3, 'Av. C, 789, Cidade Z'),
(4, 'Praça D, 321, Cidade W'),
(5, 'Alameda E, 654, Cidade V');

INSERT INTO Atendimento (id_atendimento, id_paciente, id_hospital) VALUES
(1, 1, 3),
(2, 2, 1),
(3, 3, 2),
(4, 4, 5),
(5, 5, 4);

INSERT INTO Amostras (id_amostra, data_coleta, estado_coleta, id_paciente) VALUES
(1, '2024-01-10', 'SP', 1),
(2, '2024-01-11', 'RJ', 2),
(3, '2024-01-12', 'MG', 3),
(4, '2024-01-13', 'BA', 4),
(5, '2024-01-14', 'RS', 5);

INSERT INTO Amostras (id_amostra, data_coleta, estado_coleta, id_paciente) VALUES
(6, '2024-02-20', 'SP', 1),
(7, '2024-02-21', 'RJ', 2),
(8, '2024-02-22', 'MG', 3),
(9, '2024-02-23', 'BA', 4),
(10, '2024-02-24', 'RS', 5),
(11, '2024-02-25', 'SP', 1),
(12, '2024-02-26', 'RJ', 2),
(13, '2024-02-27', 'MG', 3),
(14, '2024-02-28', 'BA', 4),
(15, '2024-02-29', 'RS', 5);


INSERT INTO Sequenciamento (id_sequenciamento, lote, data_sequenciamento, equipamento, id_relatorio) VALUES
(1, 'A123', '2024-02-01', 'EQ-01', 1),
(2, 'B456', '2024-02-02', 'EQ-02', 2),
(3, 'C789', '2024-02-03', 'EQ-03', 3),
(4, 'D321', '2024-02-04', 'EQ-04', 4),
(5, 'E654', '2024-02-05', 'EQ-05', 5);

INSERT INTO Sequenciamento_amostras (id_seq_amostra, id_amostra, id_sequenciamento) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5);

INSERT INTO Relatorios (id_relatorio, data_relatorio, observacoes, id_sequenciamento) VALUES
(1, '2024-02-15', 'Observação 1', 1),
(2, '2024-02-16', 'Observação 2', 2),
(3, '2024-02-17', 'Observação 3', 3),
(4, '2024-02-18', 'Observação 4', 4),
(5, '2024-02-19', 'Observação 5', 5);

