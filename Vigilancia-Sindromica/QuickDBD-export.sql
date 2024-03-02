-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `Pacientes` (
    `id_paciente` int NOT NULL ,
    `nome` varchar(255)  NOT NULL ,
    `data_nascimento` date  NOT NULL ,
    `sexo` char(1)  NOT NULL ,
    PRIMARY KEY (
        `id_paciente`
    )
);

CREATE TABLE `Hospitais` (
    `id_hospital` int  NOT NULL ,
    `endereco` varchar(255)  NOT NULL ,
    PRIMARY KEY (
        `id_hospital`
    )
);

CREATE TABLE `Atendimento` (
    `id_atendimento` int  NOT NULL ,
    `id_paciente` int  NOT NULL ,
    `id_hospital` int  NOT NULL ,
    PRIMARY KEY (
        `id_atendimento`
    )
);

CREATE TABLE `Amostras` (
    `id_amostra` int  NOT NULL ,
    `data_coleta` date  NOT NULL ,
    `estado_coleta` char(2)  NOT NULL ,
    `id_paciente` int  NOT NULL ,
    PRIMARY KEY (
        `id_amostra`
    )
);

CREATE TABLE `Sequenciamento` (
    `id_sequenciamento` int  NOT NULL ,
    `lote` char(5)  NOT NULL ,
    `data_sequenciamento` date  NOT NULL ,
    `equipamento` char(20)  NOT NULL ,
    `id_relatorio` int  NOT NULL ,
    PRIMARY KEY (
        `id_sequenciamento`
    )
);

CREATE TABLE `Sequenciamento_amostras` (
    `id_seq_amostra` int  NOT NULL ,
    `id_amostra` int  NOT NULL ,
    `id_sequenciamento` int  NOT NULL ,
    PRIMARY KEY (
        `id_seq_amostra`
    )
);

CREATE TABLE `Relatorios` (
    `id_relatorio` int  NOT NULL ,
    `data_relatorio` date  NOT NULL ,
    `observacoes` varchar(255)  NOT NULL ,
    `id_sequenciamento` int  NOT NULL ,
    PRIMARY KEY (
        `id_relatorio`
    )
);

CREATE TABLE `Relatorio_sequenciamento` (
    `id_rel_seq` int  NOT NULL ,
    `id_relatorio` int  NOT NULL ,
    `id_sequenciamento` int  NOT NULL ,
    PRIMARY KEY (
        `id_rel_seq`
    )
);

ALTER TABLE `Atendimento` ADD CONSTRAINT `fk_Atendimento_id_paciente` FOREIGN KEY(`id_paciente`)
REFERENCES `Pacientes` (`id_paciente`);

ALTER TABLE `Atendimento` ADD CONSTRAINT `fk_Atendimento_id_hospital` FOREIGN KEY(`id_hospital`)
REFERENCES `Hospitais` (`id_hospital`);

ALTER TABLE `Amostras` ADD CONSTRAINT `fk_Amostras_id_paciente` FOREIGN KEY(`id_paciente`)
REFERENCES `Pacientes` (`id_paciente`);

ALTER TABLE `Sequenciamento_amostras` ADD CONSTRAINT `fk_Sequenciamento_amostras_id_amostra` FOREIGN KEY(`id_amostra`)
REFERENCES `Amostras` (`id_amostra`);

ALTER TABLE `Sequenciamento_amostras` ADD CONSTRAINT `fk_Sequenciamento_amostras_id_sequenciamento` FOREIGN KEY(`id_sequenciamento`)
REFERENCES `Sequenciamento` (`id_sequenciamento`);

ALTER TABLE `Relatorio_sequenciamento` ADD CONSTRAINT `fk_Relatorio_sequenciamento_id_relatorio` FOREIGN KEY(`id_relatorio`)
REFERENCES `Relatorios` (`id_relatorio`);

ALTER TABLE `Relatorio_sequenciamento` ADD CONSTRAINT `fk_Relatorio_sequenciamento_id_sequenciamento` FOREIGN KEY(`id_sequenciamento`)
REFERENCES `Sequenciamento` (`id_sequenciamento`);

