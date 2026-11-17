# Mãos Solidárias Digital

MVP em desenvolvimento para apoiar a organização de famílias atendidas, doações, estoque e entregas em uma associação comunitária.

## Objetivo

Reunir em um só lugar as informações necessárias para acompanhar itens e suas validades, registrar entregas e reduzir retrabalho. O projeto está em fase inicial de implementação.

## Escopo planejado

- Cadastro de famílias com registro de consentimento.
- Controle de estoque por lote e alertas de validade.
- Registro de entregas com verificação de duplicidade mensal.
- Relatórios mensais.
- Interface web responsiva, com suporte planejado para uso offline.

## Tecnologias

- API: Python com FastAPI.
- Front-end planejado: Angular e Angular Material.

## API inicial

A API contém atualmente um endpoint de saúde (GET /health) e um esquema de entrada inicial para cadastro de família. Persistência, autenticação, interface web e os demais fluxos ainda estão em desenvolvimento.

### Executar localmente

A partir da raiz do repositório, crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Linux ou macOS
source .venv/bin/activate
pip install -r backend/requirements.txt
```

Inicie a API:

```bash
uvicorn app.main:app --app-dir backend --reload
```

A verificação de disponibilidade fica em http://127.0.0.1:8000/health.

## Privacidade

O esquema inicial de cadastro trabalha com contagens e exige consentimento. Não inclua dados pessoais reais em exemplos, commits ou issues deste repositório.
