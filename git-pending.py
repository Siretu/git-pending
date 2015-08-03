import os

blacklist = ['capybara-webkit-5011593cfc34','ldap_lookup-e6325728728a','spop']

def main():
    print "Searching for pending git changes"
    cmd = "find -L ~ -name .git"
    repos = os.popen(cmd).read().split('\n')[:-1]
    print "Found repos:\n%s" % str("\n".join(repos))

    modified = []
    for repo in repos:
        name = repo.split('/')[-2]
        directory = "%s/.." % repo
        if name not in blacklist:
            print "Checking for changes in %s" % name
            os.chdir(directory)
            status = os.popen("git status").read()
            if "Changes not staged for commit" in status or "Changes to be committed" in status:
                modified.append(name)
                print 'Found changes'
        else:
            print "Ignoring %s" % name

    print '----------\n%s' % '\n'.join(['Changes detected in: %s' % x for x in modified])

if __name__ == "__main__":
    main()
