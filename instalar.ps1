# Instala las habilidades del kit «estudio-ia-publica» para Codex y Cursor en Windows
# (y cualquier agente que lea la carpeta estándar %USERPROFILE%\.agents\skills).
#
#   irm https://raw.githubusercontent.com/jordansrojas1/estudio-ia-publica/main/instalar.ps1 | iex
#
# Qué hace, nada más: descarga el kit de GitHub y copia tres carpetas
# (pieza-ciudadana, auditar-diseno, referencias-visuales) en %USERPROFILE%\.agents\skills.
# Si ya tenías una carpeta con el mismo nombre, la guarda en .agents\skills-respaldo.
# Autor: Jordan Rojas · MIT · ver CREDITOS.md
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$Repo    = "jordansrojas1/estudio-ia-publica"
$Destino = Join-Path $HOME ".agents\skills"
$Tmp     = Join-Path ([System.IO.Path]::GetTempPath()) ("estudio-ia-publica-" + [guid]::NewGuid())

Write-Host ""
Write-Host "  Kit de diseño con IA para la gestión pública"
Write-Host "  Instalando para Codex y Cursor en: $Destino"
Write-Host ""

try {
  New-Item -ItemType Directory -Force -Path $Tmp | Out-Null
  $Zip = Join-Path $Tmp "kit.zip"
  Invoke-WebRequest -UseBasicParsing -Uri "https://github.com/$Repo/archive/refs/heads/main.zip" -OutFile $Zip
  Expand-Archive -Path $Zip -DestinationPath $Tmp -Force
  $Origen = Join-Path $Tmp "estudio-ia-publica-main\plugins\diseno-publico\skills"
  New-Item -ItemType Directory -Force -Path $Destino | Out-Null

  Get-ChildItem -Path $Origen -Directory | ForEach-Object {
    $Nombre = $_.Name
    $Final  = Join-Path $Destino $Nombre
    if (Test-Path $Final) {
      if (Test-Path (Join-Path $Final ".estudio-ia-publica")) {
        Remove-Item -Recurse -Force $Final                      # versión anterior del kit: se actualiza
      } else {
        $DirRespaldo = Join-Path (Split-Path $Destino -Parent) "skills-respaldo"
        New-Item -ItemType Directory -Force -Path $DirRespaldo | Out-Null
        $Respaldo = Join-Path $DirRespaldo ($Nombre + "-" + (Get-Date -Format "yyyyMMddHHmmss"))
        Move-Item $Final $Respaldo                              # carpeta ajena: se guarda fuera, no se borra
        Write-Host "  (ya tenías '$Nombre': la guardé en $Respaldo)"
      }
    }
    Copy-Item -Recurse -Path $_.FullName -Destination $Final
    Set-Content -Path (Join-Path $Final ".estudio-ia-publica") -Value "kit estudio-ia-publica"
    Write-Host "  OK $Nombre"
  }
} finally {
  Remove-Item -Recurse -Force $Tmp -ErrorAction SilentlyContinue
}

Write-Host ""
Write-Host "  ¡Listo! Cierra y vuelve a abrir Codex o Cursor."
Write-Host "  Pruébalo:  Codex -> escribe `$pieza-ciudadana   ·   Cursor -> escribe /pieza-ciudadana"
Write-Host "  Créditos: https://github.com/$Repo/blob/main/CREDITOS.md"
Write-Host ""
