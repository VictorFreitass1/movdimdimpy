CREATE TABLE tb_vagas (
    cd_vaga            NUMBER NOT NULL,
    cd_estacionamento  NUMBER NOT NULL,
    ds_localizacao     VARCHAR2(10) NOT NULL,
    ds_andar           VARCHAR2(10) NOT NULL,
    ds_disponivel      CHAR(1) NOT NULL
);

ALTER TABLE tb_vagas ADD CONSTRAINT tb_vagas_pk PRIMARY KEY ( cd_vaga );


CREATE SEQUENCE SQ_TB_VAGAS
 START WITH     1
 INCREMENT BY   1
 NOCACHE
 NOCYCLE;

INSERT INTO tb_vagas(cd_vaga, cd_estacionamento, ds_localizacao, ds_andar, ds_disponivel ) 
VALUES (SQ_TB_VAGAS.nextval,1, 'A01', 'T', '0'); -- Não está disponível

INSERT INTO tb_vagas(cd_vaga, cd_estacionamento, ds_localizacao, ds_andar, ds_disponivel ) 
VALUES (SQ_TB_VAGAS.nextval,1, 'A02', 'T', '1'); -- Disponível

commit;


SELECT * FROM tb_vagas;