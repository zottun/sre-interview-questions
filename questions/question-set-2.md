# Interview Question Set #2

Applicable to _mid-level_ or _senior_ candidates.

NB we wouldn't want a candidate spending more than a few hours on this question set - but evidently nobody is 
    timing you, so take as long as you like! This is completely open-book; use whatever resources you want.

Please submit your answers to this question set in whatever format you like; this will most likely be a text document
    containing the more 'wordy' answers, and a collection of other accompanying files/images etc. all bundled into a 
    ZIP file.
    
### 1. Troubleshooting, Cloud Security, Misc.
##### 1(a) 

Please answer the following questions, explaining how you arrived at your answers:

- What network do we proxy traffic through to our public site's back end?
- Name a subdomain that our CDN is served on.
- What Cloud Provider(s) do we use?
- Does we prefer to write backend applications in Scala or Java?
- How do we deploy our back end applications?

It is possible that one or more of these pieces of information are no longer available since the writing of this 
    Question Set. If you believe this to be the case, please state this as your answer.

##### 1(b)

Characterise a weakness in the registration flow for the ClearScore website, and suggest how it could be mitigated or 
    resolved.

##### 1(c)

We block 'bad' traffic at a number of points between client and back end, and for a variety of reasons. Find one, and 
    characterise the observed trigger(s) and blocking behaviours. 


### 2. Kubernetes, Programming, etc.

For these questions, please use `minikube` - or any flavour of 'local' Kubernetes that you are comfortable with. If you 
    have access to a real K8s cluster, you may also use that if you wish. Your answers should include deployment
    configuration that should be fully-functional and reproducible by us to verify. If something is required
    beyond simply installing `minikube`, please include details in your answer(s). If you have access to a real 
    Kubernetes cluster and would rather use that, this is also fine - we can check your answers in our own sandbox 
    clusters.
    
Submit your answer(s) in whatever form you want - that may be a single yaml file, a directory and some scripts zipped-up
    or something totally different. Make sure to include any details that we'd require to get your stuff up and running.
    
##### 2(a) 

Create a mini application stack using technologies of your choice, that satisfies the following requirements. 

- Some application(s) returns some data to http requests
- The data is persisted beyond the life of any servers
- All components are highly available
- Only one replica of a component can be unavailable at any time

##### 2(b)

Using a language of your choice, create an application and associated deployment configuration that satisfies the 
    following requirements. You may want to build an image locally and use your local Docker registry in eg. `minikube`
    - that is fine. You could also publish to a public registry or simply mount your code as a volume and run that way. 
    However you would prefer - just make sure to include instructions or scripts to help us if its not obvious!

- Runs multiple replicas, but only one is leader
- Watches K8s API for Pod creation events
- Logs some basic information about the new Pods that are created
- Exports some useful Prometheus metrics, eg. a count of new pods

*NB. We are aware that you _could_ spend a long time on this question - don't feel like you need to produce a polished 
    production-ready solution!*
