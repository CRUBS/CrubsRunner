#!/bin/bash

# Script bash pour la distribution de CrubsRunner sur Linux
# Ce script est a executer depuis le dossier CrubsRunner

rm -rf build  dist  # On fait le menage
echo "execute : python3 -m PyInstaller setup.spec"
echo ""

python3 -m PyInstaller  setup.spec

if [ -e dist/CrubsRunner ]  # On verirife que le fichier binaire a bien ete cree
then
  echo ""
  echo "Compilation reussie"
  echo ""

  echo "Copie des fichiers et dossier vers CrubsRunner_Linux"
  mkdir  CrubsRunner_Linux
  cp  dist/CrubsRunner  CrubsRunner_Linux/CrubsRunner
  cp -r  icon/  CrubsRunner_Linux/icon/
  cp -r  3d_files/  CrubsRunner_Linux/3d_files/
  cp  linux_installer.sh  CrubsRunner_Linux/linux_installer.sh

  echo ""
  echo "Compression du dossier"
  tar -zcvf CrubsRunner_Linux_v1.1.0.tar.gz  CrubsRunner_Linux

  echo ""
  echo "Construction terminee"

else
  echo ""
  echo "Compilation echouee"
fi
