# Haystack listing handoff

The package and listing draft are ready for review.
Nothing has been published or submitted.
The draft's package and repository URLs are intended destinations.
They must exist before the listing is submitted.

## Release steps

1. Review the package, tests, build artifacts, and [verification record](../.coding-agent/summary.md).
2. Create `faxforagents/haystack-tools` on GitHub after review.
3. Initialize Git locally and follow the repository's review gates before committing or pushing.
4. Push the reviewed source and make the repository public.
5. Sign in to PyPI and complete two-factor authentication.
6. Recheck the package name and configure publishing credentials through secret storage.
7. Build the reviewed release with `uv build`.
8. Publish the reviewed artifacts with `uv publish`.
9. Confirm the package page and installation from PyPI work.

PyPI returned HTTP 404 for `faxforagents-haystack` during the 2026-11-04 check.
This shows no public package existed then. It does not reserve the name or guarantee PyPI will accept it.

## Listing PR steps

1. Read the [integration index instructions](https://github.com/deepset-ai/haystack-integrations/blob/main/README.md) again before submitting.
2. Fork `deepset-ai/haystack-integrations` under an authorized GitHub account.
3. Create a branch for the Fax for Agents listing.
4. Copy [faxforagents.md](faxforagents.md) to `integrations/faxforagents.md` in the fork.
5. Confirm the package, repository, documentation, and issue links resolve.
6. Confirm frontmatter retains `type: Tool Integration` and `version: Haystack 2.0`.
7. Run the index repository's required checks.
8. Open a pull request describing the package and tested Haystack version.
9. Address maintainer feedback and wait for review.

## Ben's account steps

Ben must sign in to PyPI and complete its two-factor prompts.
Ben must provide authorized publishing access or configure a trusted publisher.
Ben must authorize GitHub access for repository creation, the fork, and the listing PR.
No accounts, repositories, releases, or pull requests were created during this build.
