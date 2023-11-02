<!DOCTYPE html>
<html>
<head>
    <title>README</title>
</head>
<body>
    <h1>DomainDossier</h1>
    <p>DomainDossier is a Python script that fetches and displays information about a domain. It uses the whois, requests, socket, ipwhois, argparse, and prettytable libraries to gather information such as nameservers, creation date, expiration date, HTTP status code, IP address, web server, hosting provider, and real hostname.</p>

    <h2>Installation</h2>
    <p>Clone the repository and install the required Python libraries:</p>
    <pre><code>git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
pip install -r requirements.txt</code></pre>

    <h2>Usage</h2>
    <p>You can use DomainDossier to get information for a single domain or a list of domains. Here are some examples:</p>
    <pre><code>python domaindossier.py -d example.com
python domaindossier.py -w domains.txt
python domaindossier.py -d example.com -o output.txt
python domaindossier.py -w domains.txt -o output.txt</code></pre>

    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
