#!/bin/bash

# release.sh - Script para empacotar e publicar nova versão do iPyScan

set -e

echo "📦 Iniciando processo de build do iPyScan..."

# Solicita versão ao usuário
read -p "Digite a nova versão (ex: 1.0.1): " version

# Atualiza a versão no setup.cfg
echo "🔧 Atualizando versão para $version..."
sed -i "s/^version = .*/version = $version/" setup.cfg

# Remove builds anteriores
echo "🧹 Limpando builds antigos..."
rm -rf dist/ build/ *.egg-info

# Gera os arquivos .tar.gz e .whl
echo "🔨 Gerando pacotes..."
python3 -m build

# Exibe resultado
echo "📁 Pacotes gerados:"
ls dist/

# Pergunta se deseja publicar
read -p "Deseja publicar no PyPI agora? (s/n): " publish

if [ "$publish" = "s" ]; then
    echo "☁️ Enviando para o PyPI..."
    twine upload dist/*
else
    echo "✅ Build finalizado. Pronto para testes locais ou push manual."
fi
