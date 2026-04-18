Please put up with me for this basic question. I am at times not sure how to navigate the official documentation efficiently.

Take the below examples(not trying to list this info via kubectl)

1. I am on the RBAC page `https://kubernetes.io/docs/reference/access-authn-authz/rbac/` and from this page I want to know how to navigate to find the all possible resources(not talking about CRDs), that I can put when creating a role.
2. Similarly, what all apiGroups are possible.

How do I find these quickly

---

## Comments

> **wolttam** · [2025-03-04](https://reddit.com/r/kubernetes/comments/1j3d3fc/comment/mfzb4y7/) · 1 points
> 
> This might help: [https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/)
> 
> > **learner\_kid\_n** · [2025-03-04](https://reddit.com/r/kubernetes/comments/1j3d3fc/comment/mfzfh95/) · 1 points
> > 
> > Thank you, I know it might sound very silly, even though that page does help to some extent but say I am trying to create a role, and I want to know what all possible resources exist, how do I even find that on that page? Maybe I am confused if the word to use is "deployment" or "deployments" from my memory and want to look at the list of resources to find the right string. Where is all this documented to be easily seen? I cannot see it on the above link, I did try to navigate using the panel on the left. I know it might sound like I just dont know how to look at the documentation, but I am really struggling with this on the k8 pages
> > 
> > > **wolttam** · [2025-03-04](https://reddit.com/r/kubernetes/comments/1j3d3fc/comment/mfzmqn1/) · 1 points
> > > 
> > > The information is all there, though yes, not in a convenient list.
> > > 
> > > This might also help: [https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources)
> > > 
> > > The command: `kubectl api-rsources` will I think show exactly what you're asking for, but needs a running cluster
> > > 
> > > The link above describes that the name to use in a rule is the same that is used in the URL for the resource. You can see the URLs resources use e.g. [here](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#read-operations-deployment-v1-apps)
> > > 
> > > **trillospin** · [2025-03-04](https://reddit.com/r/kubernetes/comments/1j3d3fc/comment/mg00obn/) · 1 points
> > > 
> > > [https://kubespec.dev/rbac.authorization.k8s.io/v1/Role](https://kubespec.dev/rbac.authorization.k8s.io/v1/Role)