I am not an expert on DNS so my answer may be mistaken, but I had the same question so looked into this.

I think your understanding is correct, and this seems to be a problem but apparently it happens rarely in practice so hosting providers (including Linode) aren't doing anything about it.

[Here](https://www.digitalocean.com/community/questions/how-does-do-verify-domain-ownership "How does DO verify domain ownership?") is Ryan Quinn from DigitalOcean (another hosting company that has this problem) answering a similar question:

> A domain can only exist on one account so any user attempting to add it would not be able to. Cases where a domain already exists or is hijacked are extremely rare (I've seen 3 cases in 2+ years and in each case it was a former owner of the domain who still had records in place). In these rare cases the user can open a support ticket where we will verify the domain whois information against their billing details to verify ownership.

[Here](https://security.stackexchange.com/questions/49612/how-does-digitalocean-dns-verify-the-owner-of-a-domain "How does DigitalOcean DNS verify the owner of a domain?") is a question on Information Security Stack Exchange that asks the same thing.

In the case of DigitalOcean, I found a [post](https://thehackerblog.com/floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-system/index.html "Floating Domains – Taking Over 20K DigitalOcean Domains via a Lax Domain Import System") ([HackerNews discussion](https://news.ycombinator.com/item?id=12364297)) of someone describing how they took over around 20,000 inactive domain names that pointed to DigitalOcean's nameservers. I haven't found anything similar for Linode, although I imagine basically the same attack is possible.

[Amazon Route 53](https://en.wikipedia.org/wiki/Amazon_Route_53) seems to use randomly generated nameservers (rather than Linode/DigitalOcean's constant `ns1.linode.com` etc.) to make this attack highly unlikely to succeed.

[Apparently](https://www.digitalocean.com/community/questions/how-does-do-verify-domain-ownership "How does DO verify domain ownership?") some other services (Google Apps?) "verify domain ownership by requiring the domain owner to add a TXT record to their domain with a special code."
