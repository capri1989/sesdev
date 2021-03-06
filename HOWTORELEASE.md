# Release Procedure

These are the steps to make a release for version `<version_number>`:

1. Make sure you are working on the current tip of the master branch.
2. Update `CHANGELOG.md` with all important changes introduced since previous version.
    - Create a new section `[<version_number>] <date YYYY-MM-DD>` and move all entries
      from the `[Unreleased]` section to the new section.
    - Make sure all github issues resolved in this release are referenced in the changelog.
    - Update the links at the bottom of the file.
3. Update version number in `sesdev.spec` to `Version: <version_number>`
4. Create a commit with title `Bump to v<version_number>` containing the
   modifications to `CHANGELOG.md` made in the previous two steps.
5. Create an annotated tag for the above commit: `git tag -s -a v<version_number>`.
    - The message should be `version <version_number>`.
    - Using `git show`, review the commit message of the annotated tag.
      It should say: `version <version_number>`.
6. Push commit and tag to github repo: `git push <remote> master --tags`
