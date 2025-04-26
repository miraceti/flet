@echo off
REM -- Forcer Java 17 pour Flutter/Flet --
set "JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-17.0.15.6-hotspot"
set "PATH=%JAVA_HOME%\bin;%PATH%"

REM -- Aller dans ton dossier projet --
cd /d D:\eric\git\flet\flet_route

REM -- Étape 1 : Laisser Flet faire son build (même s'il plante) --
flet build apk

REM -- Étape 2 : Forcer le gradle-wrapper.properties à utiliser Gradle 8.6 --
echo Patching gradle-wrapper.properties...
set "GRADLE_WRAPPER=build\flutter\android\gradle\wrapper\gradle-wrapper.properties"
if exist "%GRADLE_WRAPPER%" (
    powershell -Command "(Get-Content '%GRADLE_WRAPPER%') -replace 'distributionUrl=.*', 'distributionUrl=https://services.gradle.org/distributions/gradle-8.6-all.zip' | Set-Content '%GRADLE_WRAPPER%'"
    echo Patch OK ✅
) else (
    echo gradle-wrapper.properties introuvable ❌
    pause
    exit /b
)

REM -- Étape 3 : Relancer Flutter build apk --
echo Building APK via flutter...
D:\eric\flutter\flutter\bin\flutter.bat build apk

pause
