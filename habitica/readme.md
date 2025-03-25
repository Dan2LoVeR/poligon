<p>Для парсинга данных с сайта Habitica (включая аватар, уровень и здоровье) вам понадобится использовать их API. Вот пример кода на Python, который получает данные пользователя и выводит их в формате HTML.</p><h3>Шаг 1: Установите необходимые библиотеки</h3><div class="md-code-block"><div class="md-code-block-banner-wrap"><div class="md-code-block-banner"><div class="md-code-block-infostring">bash</div><div class="md-code-block-action"><div class="ds-markdown-code-copy-button">Copy</div></div></div></div><pre>pip <span class="token function">install</span> requests python-dotenv</pre></div><h3>Шаг 2: Создайте <code>.env</code> файл для хранения ваших API-ключей</h3><p>Создайте файл <code>.env</code> в папке с проектом и добавьте туда:</p><div class="md-code-block"><div class="md-code-block-banner-wrap"><div class="md-code-block-banner"><div class="md-code-block-infostring">env</div><div class="md-code-block-action"><div class="ds-markdown-code-copy-button">Copy</div></div></div></div><pre>HABITICA_USER_ID=ваш_user_id
HABITICA_API_TOKEN=ваш_api_token</pre></div><h3>Шаг 3: Python-скрипт для получения данных и генерации HTML</h3><div class="md-code-block"><div class="md-code-block-banner-wrap"><div class="md-code-block-banner"><div class="md-code-block-infostring">python</div><div class="md-code-block-action"><div class="ds-markdown-code-copy-button">Copy</div></div></div></div><pre><span class="token keyword">import</span> os
<span class="token keyword">import</span> requests
<span class="token keyword">from</span> dotenv <span class="token keyword">import</span> load_dotenv

<span class="token comment"># Загружаем переменные из .env</span>
load_dotenv<span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token comment"># Данные для авторизации в Habitica API</span>
USER_ID <span class="token operator">=</span> os<span class="token punctuation">.</span>getenv<span class="token punctuation">(</span><span class="token string">"HABITICA_USER_ID"</span><span class="token punctuation">)</span>
API_TOKEN <span class="token operator">=</span> os<span class="token punctuation">.</span>getenv<span class="token punctuation">(</span><span class="token string">"HABITICA_API_TOKEN"</span><span class="token punctuation">)</span>

<span class="token comment"># URL API Habitica</span>
API_URL <span class="token operator">=</span> <span class="token string">"https://habitica.com/api/v3"</span>

<span class="token keyword">def</span> <span class="token function">get_user_data</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    headers <span class="token operator">=</span> <span class="token punctuation">{</span>
        <span class="token string">"x-client"</span><span class="token punctuation">:</span> <span class="token string-interpolation"><span class="token string">f"</span><span class="token interpolation"><span class="token punctuation">{</span>USER_ID<span class="token punctuation">}</span></span><span class="token string">-MyHabiticaScript"</span></span><span class="token punctuation">,</span>
        <span class="token string">"x-api-user"</span><span class="token punctuation">:</span> USER_ID<span class="token punctuation">,</span>
        <span class="token string">"x-api-key"</span><span class="token punctuation">:</span> API_TOKEN<span class="token punctuation">,</span>
    <span class="token punctuation">}</span>
    response <span class="token operator">=</span> requests<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string-interpolation"><span class="token string">f"</span><span class="token interpolation"><span class="token punctuation">{</span>API_URL<span class="token punctuation">}</span></span><span class="token string">/user"</span></span><span class="token punctuation">,</span> headers<span class="token operator">=</span>headers<span class="token punctuation">)</span>
    <span class="token keyword">if</span> response<span class="token punctuation">.</span>status_code <span class="token operator">==</span> <span class="token number">200</span><span class="token punctuation">:</span>
        <span class="token keyword">return</span> response<span class="token punctuation">.</span>json<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token string">"data"</span><span class="token punctuation">]</span>
    <span class="token keyword">else</span><span class="token punctuation">:</span>
        <span class="token keyword">raise</span> Exception<span class="token punctuation">(</span><span class="token string-interpolation"><span class="token string">f"Ошибка при запросе: </span><span class="token interpolation"><span class="token punctuation">{</span>response<span class="token punctuation">.</span>status_code<span class="token punctuation">}</span></span><span class="token string"> - </span><span class="token interpolation"><span class="token punctuation">{</span>response<span class="token punctuation">.</span>text<span class="token punctuation">}</span></span><span class="token string">"</span></span><span class="token punctuation">)</span>

<span class="token keyword">def</span> <span class="token function">generate_html</span><span class="token punctuation">(</span>user_data<span class="token punctuation">)</span><span class="token punctuation">:</span>
    avatar_url <span class="token operator">=</span> <span class="token string-interpolation"><span class="token string">f"https://habitica.com/export/avatar-</span><span class="token interpolation"><span class="token punctuation">{</span>USER_ID<span class="token punctuation">}</span></span><span class="token string">.png"</span></span>
    level <span class="token operator">=</span> user_data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"stats"</span><span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"lvl"</span><span class="token punctuation">,</span> <span class="token string">"N/A"</span><span class="token punctuation">)</span>
    health <span class="token operator">=</span> user_data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"stats"</span><span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"hp"</span><span class="token punctuation">,</span> <span class="token string">"N/A"</span><span class="token punctuation">)</span>
    max_health <span class="token operator">=</span> user_data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"stats"</span><span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"maxHealth"</span><span class="token punctuation">,</span> <span class="token string">"N/A"</span><span class="token punctuation">)</span>

    html <span class="token operator">=</span> <span class="token string-interpolation"><span class="token string">f"""
    &lt;!DOCTYPE html&gt;
    &lt;html lang="en"&gt;
    &lt;head&gt;
        &lt;meta charset="UTF-8"&gt;
        &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
        &lt;title&gt;Habitica Stats&lt;/title&gt;
        &lt;style&gt;
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                line-height: 1.6;
            }}
            .avatar {{
                width: 140px;
                height: 147px;
                border: 1px solid #ddd;
                margin-bottom: 10px;
            }}
            .stats {{
                margin-top: 10px;
            }}
        &lt;/style&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h1&gt;Habitica Stats&lt;/h1&gt;
        &lt;div class="avatar-container"&gt;
            &lt;img src="</span><span class="token interpolation"><span class="token punctuation">{</span>avatar_url<span class="token punctuation">}</span></span><span class="token string">" alt="Habitica Avatar" class="avatar"&gt;
        &lt;/div&gt;
        &lt;div class="stats"&gt;
            &lt;p&gt;&lt;strong&gt;Level:&lt;/strong&gt; </span><span class="token interpolation"><span class="token punctuation">{</span>level<span class="token punctuation">}</span></span><span class="token string">&lt;/p&gt;
            &lt;p&gt;&lt;strong&gt;Health:&lt;/strong&gt; </span><span class="token interpolation"><span class="token punctuation">{</span>health<span class="token punctuation">:</span><span class="token format-spec">.1f</span><span class="token punctuation">}</span></span><span class="token string"> / </span><span class="token interpolation"><span class="token punctuation">{</span>max_health<span class="token punctuation">:</span><span class="token format-spec">.1f</span><span class="token punctuation">}</span></span><span class="token string">&lt;/p&gt;
        &lt;/div&gt;
    &lt;/body&gt;
    &lt;/html&gt;
    """</span></span>
    <span class="token keyword">return</span> html

<span class="token keyword">def</span> <span class="token function">save_html</span><span class="token punctuation">(</span>html_content<span class="token punctuation">,</span> filename<span class="token operator">=</span><span class="token string">"habitica_stats.html"</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">with</span> <span class="token builtin">open</span><span class="token punctuation">(</span>filename<span class="token punctuation">,</span> <span class="token string">"w"</span><span class="token punctuation">,</span> encoding<span class="token operator">=</span><span class="token string">"utf-8"</span><span class="token punctuation">)</span> <span class="token keyword">as</span> <span class="token builtin">file</span><span class="token punctuation">:</span>
        <span class="token builtin">file</span><span class="token punctuation">.</span>write<span class="token punctuation">(</span>html_content<span class="token punctuation">)</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string-interpolation"><span class="token string">f"HTML файл сохранен как </span><span class="token interpolation"><span class="token punctuation">{</span>filename<span class="token punctuation">}</span></span><span class="token string">"</span></span><span class="token punctuation">)</span>

<span class="token keyword">if</span> __name__ <span class="token operator">==</span> <span class="token string">"__main__"</span><span class="token punctuation">:</span>
    <span class="token keyword">try</span><span class="token punctuation">:</span>
        user_data <span class="token operator">=</span> get_user_data<span class="token punctuation">(</span><span class="token punctuation">)</span>
        html_content <span class="token operator">=</span> generate_html<span class="token punctuation">(</span>user_data<span class="token punctuation">)</span>
        save_html<span class="token punctuation">(</span>html_content<span class="token punctuation">)</span>
    <span class="token keyword">except</span> Exception <span class="token keyword">as</span> e<span class="token punctuation">:</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string-interpolation"><span class="token string">f"Произошла ошибка: </span><span class="token interpolation"><span class="token punctuation">{</span>e<span class="token punctuation">}</span></span><span class="token string">"</span></span><span class="token punctuation">)</span></pre></div><h3>Как получить API-ключи и User ID:</h3><ol start="1"><li><p>Зайдите в <a href="https://habitica.com" target="_blank" rel="noreferrer">Habitica</a>.</p></li><li><p>Перейдите в <strong>Настройки</strong> → <strong>API</strong>.</p></li><li><p>Скопируйте <strong>User ID</strong> и <strong>API Token</strong>.</p></li></ol><h3>Примечания:</h3><ul><li><p>Аватар генерируется по ссылке <code>https://habitica.com/export/avatar-{USER_ID}.png</code>.</p></li><li><p>Данные о здоровье и уровне берутся из API.</p></li><li><p>Если вам нужно больше данных, изучите <a href="https://habitica.com/apidoc/" target="_blank" rel="noreferrer">официальную документацию Habitica API</a>.</p></li></ul><h3>Результат:</h3><p>Скрипт создаст файл <code>habitica_stats.html</code> с вашим аватаром, уровнем и здоровьем.</p><p>Если у вас нет доступа к API или вы хотите парсить страницу напрямую (что менее надежно), можно использовать <code>BeautifulSoup</code> и <code>selenium</code>, но это сложнее и может нарушать условия использования сайта. API — рекомендованный способ.</p>