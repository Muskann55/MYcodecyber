import dns.resolver


target_domain = 'youtube.com'
records_type = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'SOA']

resolver = dns.resolver.Resolver()
for record_type in records_type:
    try:
        answer = resolver.resolve(target_domain, record_type)
    except dns.resolver.NoAnswer:
        continue
    print(f'{record_type} records for {target_domain}')
    for data in answer:
        print(f'{data}')
        
        
