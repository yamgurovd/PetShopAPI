#                                   PetShopAPI
## Автотесты API https://petstore.swagger.io/
### Для запуска автотестов необходимо:
1. Создать файл .env, прописать BASE_URL = "https://petstore.swagger.io/v2"
2. Установить все библиотеки из requirements.txt;
3. Установить Allure для просмотра результата прогонов тестов(инструкция по установке ниже)
<div class="w-full pb-4 px-4 lg:max-w-3xl"><div class="markdown-article"><h1 id="allure-report-installation">Allure Report installation</h1>
<p><img src="https://img.shields.io/maven-central/v/io.qameta.allure/allure-commandline?style=flat" alt="allure-commandline maven latest version" title="allure-commandline maven latest version"></p>
<p>Allure Report is the utility that processes test results collected by a compatible test framework and produces an HTML report. This page lists various way to install Allure Report.</p>
<h2 id="install-via-homebrew-for-macos-and-linux">Install via Homebrew (for macOS and Linux)</h2>
<ol>
<li><p>Make sure <a href="https://brew.sh/">Homebrew</a> is installed.</p>
</li>
<li><p>In a terminal, run this command:</p>
<pre class="language-bash" tabindex="0"><code class="language-bash">brew <span class="token function">install</span> allure
</code></pre>
</li>
</ol>
<h2 id="install-via-scoop-for-windows">Install via Scoop (for Windows)</h2>
<ol>
<li><p>Make sure <a href="https://scoop.sh/">Scoop</a> is installed.</p>
</li>
<li><p>Make sure Java version 8 or above installed, and its directory is specified in the <code>JAVA_HOME</code> environment variable.</p>
</li>
<li><p>In a terminal, run this command:</p>
<pre class="language-bash" tabindex="0"><code class="language-bash">scoop <span class="token function">install</span> allure
</code></pre>
</li>
</ol>
<h2 id="install-via-the-system-package-manager-for-linux">Install via the system package manager (for Linux)</h2>
<ol>
<li><p>Go to <a href="https://github.com/allure-framework/allure2/releases/latest">the latest Allure Report release on GitHub</a> and download the <code>allure-*.deb</code> or <code>allure-*.rpm</code> package, depending on which package format your Linux distribution supports.</p>
</li>
<li><p>In a terminal, go to the directory with package and install it.</p>
<ul>
<li><p>For the DEB package:</p>
<pre class="language-bash" tabindex="0"><code class="language-bash"><span class="token function">sudo</span> dpkg <span class="token parameter variable">-i</span> allure_2.24.0-1_all.deb
</code></pre>
</li>
<li><p>For the RPM package:</p>
<pre class="language-bash" tabindex="0"><code class="language-bash"><span class="token function">sudo</span> <span class="token function">rpm</span> <span class="token parameter variable">-i</span> allure_2.24.0-1.noarch.rpm
</code></pre>
</li>
</ul>
</li>
</ol>
<h2 id="install-via-npm-for-any-system">Install via NPM (for any system)</h2>
<ol>
<li><p>Make sure <a href="https://nodejs.org/">Nodejs</a> and <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm">NPM</a> are installed.</p>
</li>
<li><p>Make sure Java version 8 or above installed, and its directory is specified in the <code>JAVA_HOME</code> environment variable.</p>
</li>
<li><p>In a terminal, go to the root directory of gthe project for which you want to use Allure Report. Run this command:</p>
<pre class="language-bash" tabindex="0"><code class="language-bash"><span class="token function">npm</span> <span class="token function">install</span> --save-dev allure-commandline
</code></pre>
</li>
</ol>
<blockquote class="book-hint notes"><p>With this installation method, Allure Report only becomes available in the given project's directory. Also note that the commands for running Allure Report must be prefixed with <code>npx</code>, for example:</p>
<pre class="language-bash" tabindex="0"><code class="language-bash">npx allure-commandline serve
</code></pre>
</blockquote><h2 id="install-from-an-archive-for-any-system">Install from an archive (for any system)</h2>
<ol>
<li><p>Make sure Java version 8 or above installed, and its directory is specified in the <code>JAVA_HOME</code> environment variable.</p>
</li>
<li><p>Go to <a href="https://github.com/allure-framework/allure2/releases/latest">the latest Allure Report release on GitHub</a> and download the <code>allure-*.zip</code> or <code>allure-*.tgz</code> archive.</p>
</li>
<li><p>Uncompress the archive into any directory. The Allure Report can now be run using the <code>bin/allure</code> or <code>bin/allure.bat</code> script, depending on the operating system.</p>
</li>
</ol>
<blockquote class="book-hint notes"><p>With this installation method, the commands for running Allure Report must contain with the full path to the scripts, for example:</p>
<pre class="language-bash" tabindex="0"><code class="language-bash">D:<span class="token punctuation">\</span>Tools<span class="token punctuation">\</span>allure-2.24.0<span class="token punctuation">\</span>bin<span class="token punctuation">\</span>allure.bat serve
</code></pre>
</blockquote></div></div>


### Для запуска тестов использовать команды:
1. python -m pytest -v -s
2. allure serve или allure generate allure-results/ --clean