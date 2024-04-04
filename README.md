This tool helps setting up a Tailscale tailnet with custom oidc.

From the Tailscale documentation https://tailscale.com/kb/1240/sso-custom-oidc#webfinger-setup

> ### WebFinger setup
>
> To use a custom OIDC provider with Tailscale, you must set up a WebFinger endpoint on your domain. WebFinger verifies that you have administrative control over a domain and issuer URL discovery. For more detailed information about using WebFinger with OIDC issuer discovery, see RFC 7033.
> 
> The WebFinger endpoint must be served at https://${domain}/.well-known/webfinger and must include the issuer URL within the JRD in the response. For example:
> ```
> {
>  "subject": "acct:${email}",
>  "links": [
>    {
>      "rel": "http://openid.net/specs/connect/1.0/issuer",
>      "href": "${issuer URL}"
>    }
>  ]
>}
> ```
> The WebFinger endpoint must be hosted at the domain of the email address provided during setup. The issuer URL specified in your JRD must exactly match the issuer URL in your /.well-known/openid-configuration. For more information, refer to the Identity Provider Discovery for OpenID Connect section in the RFC 7033: WebFinger specification.

This flask server responds with the required json at the webfinger endpoint and allows you to continue setup.

I just added a entry to my reverse proxy in order to have proper certificates.
If you don't have a reverse proxy setup already, something like [Caddy](https://github.com/caddyserver/caddy) or nginx would be my go to solution.
